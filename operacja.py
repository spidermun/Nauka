import json

# import json
#
# from direct.showbase.ShadowDemo import piratesAvatarShadow
#
# baza_graczy = [
#     {
#         "id": "1",
#         "nick": "SpiderMun",
#         "level": 15,
#         "klasa": "Wojownik"
#     },
#     {
#         "id": "2",
#         "nick": "VenomXx",
#         "level": 20,
#         "klasa": "Mag"
#     }
# ]
#
# def dodaj_gracza(lista, id,nick, level, klasa):
#     nowy_gracz = {
#         "id": id,
#         "nick": nick,
#         "level": level,
#         "klasa": klasa
#     }
#     lista.append(nowy_gracz)
#     print(f"Dodano gracza {nick},{id}!")
#
# def zapisywanie_json():
#     try:
#         with open("baza_graczy.json", "w", encoding="utf-8") as file:
#             json.dump(baza_graczy, file, indent=4, ensure_ascii=False)
#         return "Zapisano pomyślnie!"
#     except Exception as e:
#         return f"Błąd zapisu: {e}"
#
# def odczytywanie():
#     try:
#         with open("baza_graczy.json", "r", encoding="utf-8") as file:
#             content = json.load(file)
#             return content
#     except FileNotFoundError:
#         print("Nie znaleziono pliku!")
#     except json.JSONDecodeError:
#         print("Plik pusty lub uszkodzony")
#
#
# dodaj_gracza(baza_graczy,3,"Cwelson",99,"Healer")
# print(zapisywanie_json())
# print(odczytywanie())

# file_path = "baza_graczy.json"
#
# def wczytaj_dane():
#     def wczytaj_graczy():
#         try:
#             with open(file_path, "r", encoding="utf-8") as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             return []
#
# def dodaj_gracza(lista, id, nick, level, klasa):
#     nowy_gracz = {
#         "id": id,
#         "nick": nick,
#         "level": level,
#         "klasa": klasa
#     }
#
#     baza_graczy.append(nowy_gracz)
#     print(f"Dodano gracza {nick},{id}!")
#
# baza_graczy = wczytaj_dane()
#
# dodaj_gracza(baza_graczy, "4","Maciek","1","minionek")
#
# with open(file_path,"w",encoding="utf-8")as file:
#     json.dump(baza_graczy,file,indent=4,ensure_ascii=False)

# import json
#
# file_path = "baza_graczy.json"
#
# def odczyt():
#     try:
#         with open(file_path,"r",encoding="utf-8")as file:
#             content = json.load(file)
#             for gracz in content:
#                 print(f"Gracz: {gracz['nick']} (Level: {gracz['level']})")
#     except json.JSONDecodeError:
#         print("blad")
#     return ""
#
# print(odczyt())

import json

slownik = {
    "gracz": "Michal",
    "level": 20
}
file_path = slownik

with open("slownik.json","w")as file:
    json.dump(slownik,file)
with open("slownik.json","r")as file:
    content = json.load(file)
    print(content)
