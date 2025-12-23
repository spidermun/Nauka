import requests


base_url = "https://pokeapi.co/api/v2/"

def get_poke_inf(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"faild to retrieve data {response.status_code}")



poke_name = "pikachu"
poke_inf = get_poke_inf(poke_name)

if poke_inf:
    print(f"{poke_inf["name"]}")