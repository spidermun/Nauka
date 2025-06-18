
import requests
import json

def main():
    is_running = True
    while is_running:
        choice_capital = input("Wybierz Stolice (np. Warszawa) lub wpisz 'koniec': ")
        if choice_capital.lower() == "koniec":
            is_running = False
            print("Koniec programu")
            continue

        api_pogoda = f"https://wttr.in/{choice_capital}?format=j1"
        response = requests.get(api_pogoda)
        if response.status_code != 200:
            print("Błąd pobierania danych pogodowych!")
            continue

        data = response.json()
        try:
            temp_C = data["current_condition"][0]["temp_C"]
            miasto = data["nearest_area"][0]["areaName"][0]["value"]
            wilgotnosc = data["current_condition"][0]["humidity"]
            opis_pogody = data["current_condition"][0]["weatherDesc"][0]["value"]
            wschod = data["weather"][0]["astronomy"][0]["sunrise"]
            zachod = data["weather"][0]["astronomy"][0]["sunset"]

            print("================================================")
            print(f"|☀️Temperatura w {miasto} to:  {temp_C}°C             ")
            print(f"️|Wilgotność w {miasto} to: {wilgotnosc}%                  ")
            print(f"️|Opis pogody w {miasto} to: {opis_pogody}               ")
            print(f"|Wschód słońca w {miasto} o godzinie: {wschod}  ")
            print(f"|Zachód słońca w {miasto} o godzinie: {zachod}  ")
            print("================================================")
        except (KeyError, IndexError):
            print("Nie udało się pobrać danych pogodowych dla tej lokalizacji.")

if __name__ == "__main__":
    main()
