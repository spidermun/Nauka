import csv
import math


#slowniki
file_path = 'sales.csv'
total_sales = 0
unikalna_data = set()
unikalny_produkt = set()
sprzedaz_produktow = {}


#kod
with open(file_path, newline='') as file:
    content = list(csv.DictReader(file))

    for row in content:
        total_sales += float(row['amount'])
    print(total_sales)

    for row in content:
        unikalna_data.add(row['date'])
    num_dnia = len(unikalna_data)
    srednia = total_sales / num_dnia
    print(f"srednia to {round(srednia, 2)} zł")

    for row in content:
        unikalny_produkt.add(row['product'])
    liczba_produktow = len(unikalny_produkt)
    print(f"Unikalnych produktów: {liczba_produktow}")

    for row in content:
        produkt = row["product"]
        kwota = float(row['amount'])
        if produkt in sprzedaz_produktow:
            sprzedaz_produktow[produkt] += kwota
        else:
            sprzedaz_produktow[produkt] = kwota

    print("Sprzedaż według produktów:")
    for produkt, suma in sprzedaz_produktow.items():
        print(f"{produkt}: {suma} zł")
