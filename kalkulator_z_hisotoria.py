from ursina import *
import random, time

app = Ursina(borderless=False)

window.title = 'F1 Race 3D'
window.size = (1200, 800)
camera.fov = 90

# Ustawienia toru
TRACK_RADIUS = 50
TRACK_WIDTH = 12
NUM_LAPS = 3
NUM_OPPONENTS = 4

# Tworzenie toru (okrągła pętla)
track = Entity(model=Mesh(vertices=[], mode='line_strip'), color=color.white, scale=1)
track_points = []
for i in range(361):
    angle = radians(i)
    x = TRACK_RADIUS * cos(angle)
    z = TRACK_RADIUS * sin(angle)
    track_points.append(Vec3(x, 0, z))

track.model.vertices = track_points
track.model.generate()

# Linia startowa
start_line = Entity(model='cube', color=color.black, scale=(TRACK_WIDTH, 0.2, 1.5),
                    position=(TRACK_RADIUS, 0.01, 0), rotation=(0, -90, 0))

# Auto gracza
player = Entity(model='cube', color=color.azure, scale=(2, 1, 4), position=(TRACK_RADIUS, 0.6, -2))
player.speed = 0
player.angle = 0  # Pozycja na torze (kąt)
player.lap = 1
player.lap_progress = 0
player.next_gate = 0
player.finished = False

# Przeciwnicy
opponents = []
opponent_colors = [color.orange, color.red, color.lime, color.violet, color.yellow]
for idx in range(NUM_OPPONENTS):
    e = Entity(model='cube', color=opponent_colors[idx % len(opponent_colors)],
               scale=(2, 1, 4), position=(TRACK_RADIUS, 0.6, 2 + idx * 3))
    e.speed = 0
    e.angle = 0
    e.lap = 1
    e.next_gate = 0
    e.finished = False
    opponents.append(e)

# Bramy kontrolne na torze (checkpointy do zliczania okrążeń)
NUM_GATES = 36
gates = []
for i in range(NUM_GATES):
    angle = i * (360 / NUM_GATES)
    x = TRACK_RADIUS * cos(radians(angle))
    z = TRACK_RADIUS * sin(radians(angle))
    g = Entity(model='cube', color=color.rgba(255,255,255,80), scale=(TRACK_WIDTH, 0.2, 0.5),
               position=(x, 0.02, z), rotation=(0, -angle, 0), visible=False)
    gates.append((angle, g))

# Mini mapa
mini_map = Entity(model='quad', texture='white_cube', color=color.rgba(50,50,50,220), scale=(.25, .25), position=(-.7, .4), parent=camera.ui)
mini_map_player = Entity(model='circle', color=color.red, scale=(.03, .03), parent=mini_map)
mini_map_opponents = [Entity(model='circle', color=opponent_colors[i], scale=(.025, .025), parent=mini_map) for i in range(NUM_OPPONENTS)]

# Kamera
camera.parent = player
camera.position = (0, 6, -13)
camera.rotation_x = 17

# UI
score_text = Text('', position=(-.85, .45), scale=2, origin=(0,0), background=True)
start_lights = [Entity(model='circle', color=color.gray, scale=.09, position=(i*0.12-0.24,0,0), parent=camera.ui, y=.25) for i in range(5)]
info_text = Text('', position=(.2, .45), scale=1.5, origin=(0,0), background=True)

# Start wyścigu - sekwencja świateł
race_started = False
lights_on = 0
countdown_time = 0
def start_sequence():
    global lights_on, race_started, countdown_time
    lights_on = 0
    race_started = False
    countdown_time = time.time()
    for l in start_lights: l.color = color.gray
    invoke(turn_on_light, 0, delay=0.7)
def turn_on_light(idx):
    global lights_on, countdown_time
    if idx < 5:
        start_lights[idx].color = color.red
        lights_on += 1
        invoke(turn_on_light, idx+1, delay=0.7)
    else:
        for l in start_lights: l.color = color.green
        global race_started
        race_started = True
        for op in opponents:
            op.speed = 0.5 + random.random() * 0.2

start_sequence()

# Reset gry
def reset():
    player.angle = 0
    player.lap = 1
    player.finished = False
    player.speed = 0
    player.position = (TRACK_RADIUS, 0.6, -2)
    player.next_gate = 0
    for i, op in enumerate(opponents):
        op.angle = 0
        op.lap = 1
        op.finished = False
        op.speed = 0
        op.position = (TRACK_RADIUS, 0.6, 2 + i * 3)
        op.next_gate = 0
    start_sequence()
    info_text.text = ""

# Logika gry
def update():
    global race_started
    if not race_started:
        return

    # Sterowanie gracza
    if not player.finished:
        steer = 0
        if held_keys['a'] or held_keys['left arrow']:
            steer = 1
        if held_keys['d'] or held_keys['right arrow']:
            steer = -1
        # Zmien kierunek jazdy (kąt na torze)
        player.angle += steer * time.dt * 45 * (player.speed / 1.5)
        player.angle %= 360

        # Przyspieszanie/hamowanie
        if held_keys['w'] or held_keys['up arrow']:
            player.speed += 0.015
        elif held_keys['s'] or held_keys['down arrow']:
            player.speed -= 0.02
        else:
            player.speed -= 0.008 # naturalne zwalnianie

        player.speed = clamp(player.speed, 0, 2.3)

        # Nowa pozycja auta gracza na torze
        x = (TRACK_RADIUS - TRACK_WIDTH/3) * cos(radians(player.angle))
        z = (TRACK_RADIUS - TRACK_WIDTH/3) * sin(radians(player.angle))
        player.position = (x, 0.6, z)
        player.rotation_y = -player.angle + 90

    # AI dla przeciwników
    for idx, op in enumerate(opponents):
        if op.finished: continue
        op.angle += (op.speed / 1.5) * 35 * time.dt
        op.angle %= 360
        # Proste AI: przyspieszają/zwalniają losowo
        if random.random() < 0.02:
            op.speed += random.uniform(-0.02, 0.025)
        op.speed = clamp(op.speed, 0.5, 2.15)
        x = (TRACK_RADIUS + TRACK_WIDTH/4 - 2 + idx) * cos(radians(op.angle))
        z = (TRACK_RADIUS + TRACK_WIDTH/4 - 2 + idx) * sin(radians(op.angle))
        op.position = (x, 0.6, z)
        op.rotation_y = -op.angle + 90

    # Detekcja okrążeń i meta
    for racer in [player] + opponents:
        if racer.finished:
            continue
        gate_angle, gate = gates[racer.next_gate]
        delta_angle = (racer.angle - gate_angle + 360) % 360
        if delta_angle < 8 or delta_angle > 352:
            racer.next_gate = (racer.next_gate + 1) % NUM_GATES
            if racer.next_gate == 0:
                racer.lap += 1
                if racer.lap > NUM_LAPS:
                    racer.finished = True
                    if racer is player:
                        info_text.text = "META! Naciśnij Enter by zresetować."
                        racer.speed = 0

    # Kolizje (prosty system)
    for op in opponents:
        if distance_2d(op.position, player.position) < 2.2 and not op.finished and not player.finished:
            player.speed *= 0.75
            op.speed *= 0.75

    # Mini-mapa
    mx = 0.1 * cos(radians(player.angle))
    mz = 0.1 * sin(radians(player.angle))
    mini_map_player.x = mx
    mini_map_player.y = mz
    for i, op in enumerate(opponents):
        mx = 0.1 * cos(radians(op.angle))
        mz = 0.1 * sin(radians(op.angle))
        mini_map_opponents[i].x = mx
        mini_map_opponents[i].y = mz

    # Wynik/pozycja/lap
    all_racers = [(player.lap, player.next_gate, -distance_2d(player.position, gates[player.next_gate][1].position), 'TY')]
    for i, op in enumerate(opponents):
        all_racers.append((op.lap, op.next_gate, -distance_2d(op.position, gates[op.next_gate][1].position), f'AUTO {i+1}'))
    all_racers.sort(reverse=True)
    pos = [x[3] for x in all_racers].index('TY') + 1
    score_text.text = f"Okrążenie: {player.lap}/{NUM_LAPS}   Pozycja: {pos}/{NUM_OPPONENTS+1}"

def distance_2d(a, b):
    return ((a.x-b.x)**2 + (a.z-b.z)**2)**0.5

def input(key):
    if key == 'enter' and (player.finished or not race_started):
        reset()

app.run()