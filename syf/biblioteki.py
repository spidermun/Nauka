import requests


base_url = "https://pokeapi.co/api/v2/"


# pobieranie danych z biblioteki requests
def get_poke_inf(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)# wysyłamy zapytanie HTTP GET i dostajemy odpowiedź


    # sprawdzamy czy api jest poprawne
    if response.status_code == 200: # 200 == wszytko ok.
        poke_data = response.json() # zamieniamy odpowiedź JSON z API na słownik Pythona
        return poke_data #jesli wszytko ok to zwracamy wczesniej pobrana
    #jesli nie jest wszytsko ok to wywalamy blad
    else:
        print(f"faild to retrieve data {response.status_code}")


poke_name = "pikachu"
poke_inf = get_poke_inf(poke_name)


#sprawdzamy czy biblioteka nie jest none.
if poke_inf:
    print(f"{poke_inf["name"]}")

