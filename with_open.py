# with open("plik.txt", "w",encoding="UTF-8" ) as file:       # dodawanie nadpisywanie do pliku
#     notatka = file.write("Dzisiaj uczę się Pythona z CS50P!")
#
# with open("plik.txt", "r",encoding="UTF-8") as file: # czytanie pliku
#     zawartosc = file.read()
#     print(zawartosc)

# wlacznik = True
# while wlacznik:
#     choice = input("Dodaj produkt do listy(q aby zakonczyc liste): ")
#     if choice == "":
#         with open("zakupy.txt","r")as f:
#             f.read()
#             print(f.read())
#         wlacznik = False
#     else:
#         with open("zakupy.txt","a")as file:
#             file.write(choice + "\n")
# wlacznik = True
# while wlacznik:
#     choice = input("Dodaj produkt do listy(q aby zakonczyc liste): ")
#     if choice == "q":  # Zmiana z "" na "q"
#         with open("zakupy.txt", "r", encoding="UTF-8") as f:
#             zawartosc = f.read()
#             print(zawartosc)  # Dodanie print()
#         wlacznik = False
#     else:
#         with open("zakupy.txt", "a", encoding="UTF-8") as file:
#             file.write(choice + "\n")

def srednia(x):
    wynik = sum(x) / len(x)
    return wynik
try:
    with open("dane.txt","r")as file:
        zawartosc = file.read()
        liczby = [float(num) for num in zawartosc.split()]
except FileNotFoundError:
    print("nie znaleziono pliku")
except ValueError:
    print("To nie liczba")
except ZeroDivisionError:
    print("Nie dziel przez zero")
finally:
    print(srednia(liczby))
