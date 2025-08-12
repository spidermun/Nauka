'''
Nauka GIta
'''
# najwazniejsze inormacje o GIT/komendy
# git status
# git add .
# git log
# git commit -m "komentarz"

# dodaje wszystkie zmiany do stage
# git commit -m "komentarz"  # tworzy commit z komentarzem
# git push origin main  # wysyla zmiany na zdalne repozytorium
# git pull origin main  # pobiera zmiany z zdalnego repozytorium
# git branch  # pokazuje listę gałęzi
# git checkout -b nazwa_gałęzi  # tworzy nową gałąź i przechodzi na nią
# git merge nazwa_gałęzi  # scala zmiany z innej gałęzi do bieżącej
# git log  # pokazuje historię commitów
# git reset --hard HEAD  # resetuje zmiany do ostatniego commita
# git stash  # tymczasowo zapisuje zmiany, aby móc przełączyć się na inną gałąź
# git stash pop  # przywraca ostatnio zapisane zmiany ze stash
# git remote add origin
# git remote -v  # pokazuje zdalne repozytoria
"""
====================================
SEKCJA: ZMIENNE
====================================
"""
# result = name.find('o')
# result = name.rfind("q")
# name = name.capitalize() powieksza 1 litere wszytkie inne sa zmieniane na mala litere
# name = name.upper() # zmienia wszytko na duze
# name = name.lowwer() # zmienia na wszystko na mniejsze
# result = name.isdigit() # sprawdza czy wszytko jest cyframi jesli nie da false
# result = name.isalpha() # sprawdza czy wszytko jest literami i tylko literami
# numer_telefonu = numer_telefonu.isdigit()
# result = numer_telefonu.count("-","")
# print(numer_telefonu)
# username = input(f"Wpisz swoja nazwe: ")
# username.find(' ')
# .isalnum
#
# if len(username) > 12:
#     print("twoj Nick nie moze miec wiecej niz 12 znakow")
# elif not username.find(' ')== -1:
#     print('twoj nik nie moze zawierac spacji')
# elif not username.isalpha():
#     print('Twoj nick nie moze zawierac cyfr')
# elif not username.capitalize()== username:
#     print('nick musi zaczerpniac pierwsza litere')
# else:
#     print(f"Witaj {username}")
# username = input('wpisz swoj nick: ')
# if len(username) > 12:
#     print("twoj nick nie moze miec wiecej niz 12 znakow")
# elif not username.find(' ')== -1:
#     print('twoj nick nie moze zawierac spacji')
# elif not username.isalpha():
#     print('twoj nick nie moze zawierac cyfr')
# else:
#     print(f'Witaj {username}')
"""
====================================
SEKCJA: OPERATORY : 
====================================
#indeksowanie to przypisanie numeru do kazdego znaku w stringu [] (indexing operator)
# [start:stop:step]
====================================
"""
# indeksowanie to przypisanie numeru do kazdego znaku w stringu [] (indexing operator)
# [start:stop:step]

# nr_kredytowy = "1697-1866-1338"
# #print(numer[3:4:5])
# #print(numer[:5]) ":" znacza od poczatku do 5 znaku
# # print(numer[5:9]) ":" znacza od 5 do 9 znaku
# # print(numer[0:)  ":"znacza od poczatku do konca
# #print(numer[-1]) "-" znacza od ostatniej liczby
# # print(numer[::2]) # "::" znacza co druga liczbe
#
# ostatni_nr = nr_kredytowy[-4:]
# print(f"XXXX-XXXX-XXXX-{ostatni_nr}")

#  specyfikatory formatu = {wartość:flagi} formatują wartość na podstawie
#  tego, jakie flagi zostaną wstawione

# .(numer)f = zaokrągla liczbe do ilosci liczb po przecinku np. {:.2f} = 2 liczby po przecinku
# :(numer) = rezerwuje ilosc znakow na liczbie np. {:5} = 5 znakow
# :03 = rezerwuje i uzupelnia zerami tyle miejsc
# :< = wyrównuje do lewej
# :> = wyrównuje do prawej
# :^ = wyrównuje do srodka
# :+ dodaje znak plus dla wartosci dodatnich
# :, dodaje przecinek co 3 cyfry
# := umieszcza znak na skrajnej lewej stronie
# : (spacja) dodaje spacje dla wartosci dodatnich
# :_ dodaje podkreslenie dla wartosci dodatnich
# W wyrażeniu f"Cena 1 jest {cena2:.2f}" zapis :.2f to specyfikator formatu, który oznacza:
#
# : → Wskazuje początek formatu w klamrach {}.
# .2 → Oznacza, że liczba zostanie zaokrąglona do 2 miejsc po przecinku.
# f → Wskazuje, że liczba powinna być sformatowana jako liczba zmiennoprzecinkowa (ang. fixed-point notation).

#
# cena1 = 3000.14159
# cena2 = -987.65
# cena3 = 1200.34
#
# print(f"Cena 1 jest {cena1:,.2f}")
# print(f"Cena 1 jest {cena2:,}")
# print(f"Cena 1 jest {cena3:,}")
"""
====================================
SEKCJA: PĘTLE
====================================
"""
# while loop = pętla nieskończona
# imie = input(f"Wpisz Swoje imie:")
# while imie == "":
#     print(f'Witaj {imie}')


# imie = input(f"Wpisz Swoje imie:")
# while imie == "":
#     print('musisz podac swoje imie')
#     imie = input(f"Wpisz Swoje imie:")
#     print(f'Witaj {imie}')


# wiek = int(input("wpisz swoj wiek: "))
#
# while wiek < 0:
#     print("wiek nie moze byc ujemny")
#     wiek = int(input("wpisz swoj wiek: "))
# print(f'Twoj wiek wynosi: {wiek}')

# jedzenie = input(f'wpisz jaedzienie jakie lubisz(wpisz q aby wyjsc):')
# while not jedzenie == 'q':
#     print(f'Ty lubisz {jedzenie}')
#     jedzenie = input(f"podaj inne jedzenie ktore lubisz(lub wpisz q aby wyjsc): ")
#
# print("bywaj")
# num = int(input("wpisz liczbe od 1-10:"))
#
# while num < 1 or num > 10:
#     print(f'{num} nie jest poprawny')
#     num = int(input("wpisz liczbe od 1-10:"))
# print(f'Twoj numer to {num}')
# print(f'Twoj numer to {num}')
# print(f'Twoj numer to {num}')
#
# PĘTLA FOR
#   reversed(range(1,11,2)):
#
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)
# if x == 13: # to np nie wyswietli 13
#     continue
#
# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)
#
#
# for x in range(3):
#     for y in range(1,11):
#         print(y,end="")
#     print()
#
# wiersze = int(input("Wpisz ilosc # w wierszu: "))
# kolumny = int(input("Wpisz ilosc # w kolumny: "))
# symbol = input("wpisz symbol jaki chcesz uzyc: ")
#
# for x in range(wiersze):
#     for y in range(kolumny):
#         print(symbol, end='')
#     print()
#
'''
====================================
SEKCJA: Kalkulator
====================================
'''
# python kakulator procentu skladanego

# zasada = 0
# rata = 0
# czas = 0
#
# while zasada <= 0:
#     zasada = float(input("Wpisz kwote zasady: "))
#     if zasada <= 0:
#         print("Kwota musi byc wieksza niz 0")
#
# while rata  <= 0:
#     rata = float(input("Wpisz kwote raty: "))
#     if rata <= 0:
#         print("Kwota musi byc wieksza niz 0")
#
# while czas <= 0:
#     czas = float(input("Wpisz czas w latach: "))
#     if czas <= 0:
#         print("Czas musi przekraczac 0")
# print(zasada)
# print(rata)
# print(czas)
#
# total = zasada * pow((1 + rata / 100),czas)
# print(f"Balans po {czas} latach wynosi ${total:.2f}")


# zasada = 0
# rata = 0
# czas = 0
#
# while True:
#     zasada = float(input("Wpisz kwote zasady: "))
#     if zasada <= 0:
#         print("Kwota musi byc wieksza niz 0")
#     else:
#         break
#
# while True:
#     rata = float(input("Wpisz kwote raty: "))
#     if rata < 0:
#         print("Kwota musi byc wieksza niz 0")
#     else:
#         break
#
# while True:
#     czas = float(input("Wpisz czas w latach: "))
#     if czas < 0:
#         print("Czas musi przekraczac 0")
#     else:
#         break
# # print(zasada)
# # print(rata)
# # print(czas)
#
# total = zasada * pow((1 + rata / 100),czas)
# print(f"Balans po {czas} latach wynosi ${total:.2f}")
#
'''
====================================
SEKCJA: Time
====================================
'''
# import time
#
# moj_czas =int(input("wpisz swoj czas w sekundach: "))
#
# for x in range(moj_czas, 0,-1):
#     sekundy = x % 60
#     minuty = int(x / 60)%60
#     godziny = int(x / 3600)
#     print(f"{godziny:02}:{minuty:02}:{sekundy:02}")
#     time.sleep(1)
#
# print('Czas wstawac')
# import random
# wybor = random.choice(['papier','kamien','nozyce'])
# print(f'wylosowal sie {wybor}')
'''
====================================
SEKCJA: listy
====================================
'''
# # lista = [] porzątkuje i zmienia mozna dublikowac
# # set = {} # wartosci sa nieuporzadkowane i niezmienne
# # tuple = () # nieuporzadkowane nie zmienia mozna dublowac szybko
# tablica = ['japko','pomarancza','jajko','kiwi']
# # print(dir(tablica))
# # print(help(tablica))
# # print(len(tablica))
# # print("pineapple" in tablica) # sprawdza czy element jest w tablicy
# # tablica.remove('pineapple') # usuwanie elementu
# tablica.sort()
# tablica.reverse() # odwraca kolejnosc
# # tablica.clear()
# tablica.append('banan') # dodaje element na koncu
# print(tablica)
# tablica.remove('banan')
# print(tablica)
# tablica.pop()
# print(tablica)# usuwa ostatni element/ usuwa losowo
'''
====================================
SEKCJA: Shooping cart program
====================================
'''
# jedzenie = []
# ceny = []
# total = 0
# while True:
#     jedzenie= input('Wpisz jedzenie jakie chcesz kupic:(q aby wyjsc): ')
#     # if  jedzenie == "q" or jedzenie == "Q":
#     if jedzenie.lower() == "q":
#         print("wyszedles ze sklepu")
#         break
#     else:
#         cena = float(input(f'wpisz cene jedzenia {jedzenia}: '))
#         jedzenie.append(jedzenia)
#         cena.append(cena)

# jedzenie = []
# ceny = []
# total = 0
# while True:
#     item = input('Wpisz jedzenie jakie chcesz kupic:(q aby wyjsc): ')
#     if item.lower() == "q":
#         # print("wyszedles ze sklepu")
#         break
#     else:
#         cena = float(input(f'wpisz cene jedzenia {item}: '))
#         jedzenie.append(item)
#         ceny.append(cena)
# print("===twoj koszyk ===")
# for item in jedzenie:
#     print(item, end=" ")
#
# for cena in ceny:
#     total += cena
# print(total)
# print(f'twoj total jest warty {total}$ ')
# print("dowidzenai zapraszam ponownie")
'''
====================================
SEKCJA: 2dlist
====================================
'''
#
# owoce = ['banan','jablko','pomarancza']
# warzywa = ['marchewka','ziemniak','kapusta']
# mieso = ['kurczak','wieprzowina','wołowina']
#
# artykuly = [owoce,warzywa,mieso]
#
# # print(artykuly[2][0]) # 1 nawias [] to lista a 2 nawias [] to element w liscie
# for kolekcja in artykuly:
#     for food in kolekcja:
#         print(food, end=" ")
#     print()
# '''
# ====================================
# podpunkt klawiatura 2d
# ====================================
# '''
# num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
#
# for wiersz in num_pad:
#     for num in wiersz:
#         print(num, end=" ")
#     print()
'''
====================================
SEKCJA: quizgame
====================================
'''
# pytania = ("Najwiekszy ssak na swiecie?: ","bitwa pod grunwaldem: ","Kiedy byl koniec II wojny swiatowej?: ")
#
# opcje = (("A. Słon ","B. Człowiek","C. wieloryb"),
#          ("A. 1510","B. 1511","C. 1410"),
#          ("A. 20 Kwietnia 1945","B. 1 Wrzesnia 1939 ","C. 8 Maja 1945"))
# odpowiedzi = (("C"),("C"),("C"))
# odgadniete = []
# wynik = 0
# pytania_num = 0
#
# for pytanie in pytania:
#     print("==============")
#     print(pytanie)
#     for opcja in opcje[pytania_num]:
#         print(opcja)
#     odpowiedz = input("Wybierz odpowiedz: ")
#     odgadniete.append(odpowiedz)
#     if odpowiedz.upper() == odpowiedzi[pytania_num]:
#         wynik += 1
#     else:
#         print(f"Poprawna odpowiedz to: {odpowiedzi[pytania_num]}")
#     pytania_num += 1
# print("==============")
# if wynik >= 2:
#     print("Gratulacje zdales")
#     print(f"twoj wynik to {wynik}/3")
# else:
#     print("Niestety nie zdales")
#     print(f"twoj wynik to {wynik}/3")
# print("================")
# print("twoje odzpowiedzi to: ")
# for odpowiedz in odgadniete:
#     print(odpowiedz, end="")
# print()
# print("==============")
# print("Dziekuje za gre")
''' 
====================================
SEKCJA: słownik pary klucz-wartość
====================================
słownik to zbior par np {klucz"wartosc} nie mozna powtarzac
===================================
'''
# słownik to zbior par np {klucz"wartosc} nie mozna powtarzac
# stolica = {"USA":"Waszyngton",
#            "Japonia":"Tokio",
#            "Chiny":"Pekin",
#            "Polska":"Warszawa"}
# print(dir(stolica))
# print(help(stolica))
# print(stolica.get("USA")) .get pozwala sprawdzic czy klucz istnieje czyli jesli jest np USA i jest jej stolica to zworci stolice jesli nie to zworci None, a nie blad
# if stolica.get("Rosja"):
#     print("Stolica istnieje")
# else:
#     print(f"Stolica nie istnieje")
# stolica.update({"Niemcy":"Berlin"}) # dodaje nowy element do slownika LUB zmienia to co juz jest w slowniku np.
# stolica.update({"Niemcy":"Warszawa"})
# print(stolica.get("Niemcy"))
# stolica.pop("USA")
# stolica.clear()
# keys = stolica.keys() # .keys() pozwala zobaczyć wszystkie klucze w słowniku.
#
# for key in stolica.keys():
#     print(key)

# wartosci = stolica.values() # .values() pozwala zobaczyć wszystkie wartości w słowniku.
# print(wartosci)
# for wartosc in stolica.values():
#     print(wartosc)
# items = stolica.items()# .items() pozwala zobaczyć wszystkie pary klucz-wartość w słowniku.
# print(items)
# for item in stolica.items():
#     print(item)
# for key,value in stolica.items():
#     print(f'{key}: {value}')
''' 
====================================
SEKCJA:Program do nauki tematu wyzej ^
====================================
'''

# menu = {
# "pizza":12.00,
# "taco":5.00,
# "burger":8.00,
# "sushi": 10.00
# }
# koszyk = []
# total = 0
# print("=====MENU=====")
# for key,value in menu.items():
#     print(f"{key:7}: ${value:.2f}")
# print("==============")
# while True:
#     jedzenie = input("wpisz jedzenie jakei chcesz wybrac (q aby wyjsc): ").lower()
#     if jedzenie == "q":
#         break
#     elif menu.get(jedzenie) is not None:
#         koszyk.append(jedzenie)
# print("======TWOJE ZAMOWIENIE ========")
# for jedzenie in koszyk:
#     total += menu.get(jedzenie)
#     print(jedzenie, end=" ")
#
# print()
# print(f"Całosc to:  ${total:.2f}")
# print("==============")
''' 
====================================
SEKCJA:szybki temat random
====================================
'''
# import random
# low = 1
# high = 20
# opcje = ("papier","kamien","nozyce")
# karty = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
# # numer = random.randint(low, high)
# # opcja = random.choice(opcje)
# # random.shuffle(karty) # .shuffle pokazuje tylko np 3 ale wszytkie w randomowo posortowanej kolejnosci
#
# print(karty)
''' 
====================================
SEKCJA: Gra w zgadywanie liczb/papier kamien nozyce
====================================
'''
# import random
#
# min_liczb = 1
# max_liczb = 99
# odpowiedz = random.randint(min_liczb, max_liczb)
# jest_wlaczane = True
#
# print("Witaj w grze Zgadywanie Liczb!")
# print(f"Wybierz liczbę od {min_liczb} do {max_liczb}")
#
# while jest_wlaczane:
#     odgadniete = input("Wpisz swoją odgadniętą liczbę: ")
#     if odgadniete.isdigit():
#         odgadniete = int(odgadniete)
#         if odgadniete < min_liczb or odgadniete > max_liczb:
#             print("Wybierz liczbę, która mieści się w przedziale!")
#         elif odgadniete < odpowiedz:
#             print("Za mała!")
#         elif odgadniete > odpowiedz:
#             print("Za duża!")
#         else:
#             print(f"Gratulacje! Odgadłeś liczbę: {odpowiedz}")
#             jest_wlaczane = False
#     else:
#         print("Wpisz poprawną liczbę!")
#     print(f"Proszę wpisz odpowiednią liczbę od {min_liczb} do {max_liczb}")
#

# import random
# low = 1
# high = 10
# answer = random.randint(low, high)
# guess = 0
# is_turn = True
#
# print("=======Witamy w grze!!!=======")
# while is_turn:
#     guess = input(f"Wpisz liczbe od {low} do {high}: ")
#     if guess.isdigit():
#         guess = int(guess)
#         if guess < low or guess > high:
#             print("wybierz odpowiedz w przedziale!")
#         elif guess < answer:
#             print("odpowiedz jest za mala")
#         elif guess > answer:
#             print("odpowiedz jest za duza")
#         else:
#             print(f"Gratulacje odgadles liczbe: {answer}")
#             is_turn = False
#     else:
#         print("Proszę wpisać poprawną liczbę!")
#     print("=============================")
# import random
#
# low = 1
# high = 10
# answer = random.randint(low, high)
# guess = 0
# is_turn = True
#
# print("Witam w grze!")
# while is_turn:
#     guess = input(f"Wpisz liczbe od {low} do {high}: ")
#     if guess.isdigit():
#         guess = int(guess)
#         if guess < low or guess > high:
#             print(f"Liczba poza przedzialu! Wybierz liczbe z przedzialu! Od {low} do {high}: ")
#         elif guess < answer:
#             print("odpwiedz jest za mala")
#         elif guess > answer:
#             print("odpwiedz jest za duza")
#         elif guess == answer:
#             print("================")
#             print("Gratulacje!")
#             print(f"Odgadles liczbe: {answer}")
#             print('=================')
#             is_turn = False
#     else:
#         Print("wpisz liczbe z przedzialu!")
# if gracz.lower() in opcje:
#     print(f"Gracz wybrał: {gracz}")
#     print(f"Komputer wybrał: {odpowiedz}")
#     if gracz == odpowiedz:
#         print("Remis!")
#     elif (gracz == "kamien" and odpowiedz == "nozyce") or \
#             (gracz == "papier" and odpowiedz == "kamien") or \
#             (gracz == "nozyce" and odpowiedz == "papier"):
#         print("Gratulacje! Wygrałeś!")
#     else:
#         print("Niestety przegrałeś!")
# else:
#     print("Wybierz poprawną opcję!")
''' 
====================================
SEKCJA: function/def
====================================
#function = jest to zbiór instrukcji, które można wielokrotnie wykorzystywac w kodzie np. def nazwa_funkcji(parametry):
# postaw () po  nazwie funkcji aby ja uruchomic
# return = zwraca wartosc z funkcji
# i wysyla je spowrotem
====================================

'''
# function = jest to zbiór instrukcji, które można wielokrotnie wykorzystywac w kodzie np. def nazwa_funkcji(parametry):
# postaw () po  nazwie funkcji aby ja uruchomic
# return = zwraca wartosc z funkcji
# i wysyla je spowrotem

# def display_invoice(username, amount, due_date):
#     print(f"Witaj {username}")
#     print(f'Twoj rachunek wynosi: {amount:.2f}$ czas zaplaty to {due_date}')
# display_invoice("Jan Kowalski", 40.50, "03/05/2025")


# def add(x,y):
#     z = x + y
#     return z
#
# def sub(x,y):
#     z = x - y
#     return z
#
# def multi(x,y):
#     z = x * y
#     return z
#
# def divide(x,y):
#     z = x / y
#     return z
#
# print(add(2,3))
# print(sub(2,3))
# print(multi(2,3))
# print(divide(2,3))
# def stworz_imie(imie,nazwisko):
#     imie = imie.capitalize()
#     nazwisko = nazwisko.capitalize()
#     return imie +  " " + nazwisko
#
# imie_od_usera = input("Podaj swoje imię: ")
# nazwisko_od_usera = input("Podaj swoje nazwisko: ")
#
# cale_imie = stworz_imie(imie_od_usera, nazwisko_od_usera)
# print(cale_imie)
''' 
====================================
SEKCJA: to samo co wyzej tylko z argumentami
====================================
# podstawowe argumenty = to Domyślna wartość dla określonych parametrów.
# Wartość domyślna jest używana, gdy argument zostanie pominięty.
# Umożliwia tworzenie bardziej elastycznych funkcji oraz zmniejsza liczbę wymaganych argumentów.
====================================
'''

# podstawowe argumenty = to Domyślna wartość dla określonych parametrów.
# Wartość domyślna jest używana, gdy argument zostanie pominięty.
# Umożliwia tworzenie bardziej elastycznych funkcji oraz zmniejsza liczbę wymaganych argumentów.

# def net_price(price,discount = 0, tax=0.05):
#     return price * (1 - discount) * (1 + tax)
# # print(net_price(500))
# print(net_price(500, 0.5))


# import time
# def cena(koniec,start=0):
#     for x in range(start,koniec+1):
#         print(x)
#         time.sleep(1)
#     print("zrobione")
# cena(10)

#  keyword arguments = to argumenty, które są przekazywane do funkcji w postaci par klucz-wartość.
#                    Umożliwia to przekazywanie argumentów w dowolnej kolejności, co zwiększa elastyczność funkcji.
#
# def czesc(powitanie, tytuł,imie,nazwisko):
#     print(f"{powitanie} {tytuł} {imie} {nazwisko}")
# czesc("Witaj",tytuł="Panie",nazwisko="cwelowski",imie="cwel")
# for x in range(1,11):
#     print(x,end="  ")
# print("1","2","3","4", sep="_-_-_")
# def get_phone(kraj,region,frist,last):
#     return f"{kraj}--{region}--{frist}-{last}"
# num_tel = get_phone(region=+48,kraj=23,frist=345,last=5433)
# print(num_tel)
''' 
====================================
SEKCJA: **kwargs i *args
====================================
# **kwargs =to argumenty, które są przekazywane do funkcji w postaci słownika.
#           Umożliwia to przekazywanie dowolnej liczby argumentów w postaci par klucz-wartość.
# *args =   to argumenty, które są przekazywane do funkcji w postaci krotki.
#           Umożliwia to przekazywanie dowolnej liczby argumentów w postaci krotki.
====================================
'''
# **kwargs =to argumenty, które są przekazywane do funkcji w postaci słownika.
#           Umożliwia to przekazywanie dowolnej liczby argumentów w postaci par klucz-wartość.
# *args =   to argumenty, które są przekazywane do funkcji w postaci krotki.
#           Umożliwia to przekazywanie dowolnej liczby argumentów w postaci krotki.
#
#
# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(add(1, 2, 3,5))


# def display_name(*args):
#     for arg in args:
#         print(arg,end=" ")
# # display_name("Dr.","Dawid","cwel","Tocwel")
# def print_address(**kwargs):
#    for key,wartosc in kwargs.items():
#        print(f'{key}: {wartosc}')
#               #klucz #wartosc
# print_address(ulica="Pitulica",mieszkania="12",miasto="Warszawa",kod_pocztowy="22-300",kraj="Polska")


# def shipping_address(*args,**kwargs):
#     for arg in args:
#         print(arg,end=" ")
#     print()
#     if "apt" in kwargs:
#         print(f"Z: {kwargs.get('city')} #{kwargs.get('apt')}")
#     elif "POBOX" in kwargs:
#         print(f"Z: {kwargs.get('city')} #{kwargs.get('POBOX')}")
#     else:
#         print(f"Z: {kwargs.get('city')}")
#     print (f"W :{kwargs.get('country')}")
# shipping_address("Dr.","Patryk","Rozgwiazda","II",
#                  city="Bikinidolne",country="Wyspy Marshalla",apt="12",
#                  )
# cwel
''' 
====================================
SEKCJA:internowane
====================================

#internowany = to obiekty, które można iterować, czyli przechodzić przez nie jeden element po drugim. Moze byc petla
'''
# internowany = to obiekty, które można iterować, czyli przechodzić przez nie jeden element po drugim. Moze byc petla

#         #klucz="A" #wartosc="1"
# biblioteka = {"A":1, "b":2,}
# for key,value in biblioteka.items(): #biblioteka.items():jesli chcemy oba uzywamy tej metody .items
# print(f"{key} = {value}")                    # #biblioteka.values(): jesli chcemy sama wartosc to uzywamy tej metody .values
''' 
====================================
SEKCJA:Operatory przynależności
====================================
#   Operatory przynależności  Służą one do sprawdzania, czy dany element znajduje się w danej strukturze danych
#       (np. liście, krotce, słowniku, zbiorze). Są to operatory, które pozwalają na szybkie sprawdzenie, czy element "należy" do tej struktury.

'''
#   Operatory przynależności  Służą one do sprawdzania, czy dany element znajduje się w danej strukturze danych
#       (np. liście, krotce, słowniku, zbiorze). Są to operatory, które pozwalają na szybkie sprawdzenie, czy element "należy" do tej struktury.

# word ="apple"
# letter = input(f"Guess a letter in the secret word:")
#
# if letter not in word:
#     print(f"bad joob the letter is {letter}")
# else:
#     print(f"good joob the letter is {letter}")
# uczniowie = {"Michal","Patryk","Ola"}
# student = input("wpisz swojego ucznia: ").capitalize()
# if student in uczniowie:
#     print(f"{student} jest w klasie")
# else:
#     print(f"{student} nie jest w klasie")
# Oceny = {"Ola":"5","Patryk":"4","Michał":"3"}
# uczen = input("Wpisz imie ucznia: ").capitalize()
#
# if uczen in oceny:
#     print(f"{uczen} ma ocene {oceny[uczen]}")
# else:
#     print(f"{uczen} nie znaleziony")
# email = "mtrela@gmial.com"
#
# if "@" in email and "." in email:
#     print("Poprawny email")
# else:
#     print("niepoprawny email")
''' 
====================================
SEKCJA:listy kompresyjne 
====================================
# Listy kompresyjne = to sposób na tworzenie list w Pythonie.
# Są bardziej kompaktowe i prostsze do odczytania niż tradycyjne pętle.
# [wyrażenie for wartości in iterowalnym if warunku]
'''
# Listy kompresyjne = to sposób na tworzenie list w Pythonie.
# Są bardziej kompaktowe i prostsze do odczytania niż tradycyjne pętle.
# [wyrażenie for wartości in iterowalnym if warunku]


# dubles = [x * 2 for x in range(1,11)]
# tripels = [y * 3 for y in range(1,11)]
# po4rny = [z*4 for z in range(1,11)]
# print(dubles)
# print(tripels)
# print(po4rny)
# Owoce = ["banan","jablko","pomarancza","kiwi"]
# Owoce_literki = [owoc[0] for owoc in Owoce]
# print(Owoce_literki)
# numbers = [-1,1,-2,-3,3,-4,]
# plus_nums = [num for num in numbers if num >=0]
# minus_nums = [num for num in numbers if num <0]
# parzyte_nums =[num for num in numbers if num % 2 == 0]
# nieparzyte_nums =[num for num in numbers if num % 2 == 1]
# print(minus_nums)
# print(plus_nums)
# print(parzyte_nums)
# print(nieparzyte_nums)
# oceny = [74,85,99,4,30,75,53]
# zdane_oceny = [ocena for ocena in oceny if ocena >= 51]
# print(zdane_oceny)
''' 
====================================
SEKCJA:Match-case statement
====================================
# Match-case statement = to instrukcja warunkowa, która pozwala na porównanie wartości z różnymi przypadkami.
# Jest to bardziej elastyczna i czytelna alternatywa dla instrukcji if-elif-else.
# Umożliwia to łatwe dopasowanie wartości do różnych wzorców i wykonanie odpowiednich działań w zależności od dopasowania.
# zalety:czytelniejszy kod, mniej linijek kodu
'''
# def is_weekend(day):
#     match day:
#         case  "Ponideziałek" | "Wtorek" | "Sroda" | "Czwartek" | "Piątek":
#             return False
#         case 'sobota' | "Niedziela":
#             return True
#         case _:
#             return "Niepoprawny dzień tygodnia"
# print(input("Wpisz dzien tygodnia: ").capitalize())


'''
====================================
SEKCJA:module
====================================
module = to plik z kodem Pythona, który można zaimportować do innego pliku Pythona.
Można w nim zdefiniować funkcje, klasy i zmienne, które można później używać w innych plikach Pythona.
mozesz tez samemu zbudowac i zimportowac 
====================================
'''
# import math
# import math as m #nadaje imie
# import math import pi
# print(pi)
# import cwiczenie
#
# result = cwiczenie.pi
# result = cwiczenie.square(3)
# result = cwiczenie.cube(3)
# result = cwiczenie.obwod(3)
# result = cwiczenie.area(3)
# print(result)
'''
====================================
SEKCJA:
====================================
Variable scope = zakres zmiennej, czyli miejsce, w którym zmienna jest widoczna i dostępna.
Scope resolution = rozwiązywanie zakresu, czyli proces określania, która zmienna jest używana w danym kontekście.LEGB Rule,(local -> enclosed -> global -> built-in)
====================================
'''
# (local -> enclosed -> global -> built-in)
# def fun1():
#     print(x)
#
# def fun2():
#     print(x)
#
# x = 3
#
#
# fun1()
# fun2()
# from math import e
# def fun1():
#     print(e)
# e = 3
# fun1()
'''
====================================
SEKCJA:if __name__ == "__main__":
====================================
ten skrypt jest importowany ALBO uruchamiany samodzielnie
funckje i clasy w tym module moga byc wykorzystane ponownie
poza glownym skrypten

biblioteka = zaimportowana biblioteka dla funkcjonalności
jeśli biblioteka jest uruchamiana bezpośrednio, wyświetl stronę pomocy
====================================
'''
# moj program
# programy sa w plikach script1.py, script2.py
'''
====================================
SEKCJA:Program Bank
====================================
'''
# def show_balance(balance):
#     print(f"twoj balance wynosi:${balance:.2f}$")
#
# def deposit(balance):
#     kwota = float(input("wpisz deponowana kwote: "))
#     if kwota < 0:
#         print("kwota niepoprawna")
#         return 0
#     else:
#         return kwota
#
# def withdraw(balance):
#     kwota = float(input("Wpisz wyplacana kwote:"))
#     if kwota > balance:
#         print("kwota niepoprawna")
#         return 0
#     elif kwota < 0:
#         print("kwota niepoprawna")
#         return 0
#     else:
#         return kwota
# def main():
#     balance = 0
#     is_running = True
#
#
#     while is_running:
#         print("banking program")
#         print("1.show balance")
#         print("2. deposit")
#         print("3. withdraw")
#         print("4. exit")
#
#         choice = input("wybierz opcje (1-4):")
#         match choice:
#             case "1":
#                 show_balance(balance)
#             case "2":
#                 balance += deposit(balance)
#             case "3":
#                 balance -= withdraw(balance)
#             case "4":
#                 print("Wyjscie z programu")
#                 is_running = False
#             case _:
#                   print("Niepoprawny wybór, spróbuj ponownie")
#
#     print("Dziekujemy, MIłego dnia!")
# if __name__ == "__main__":
#     main()
'''
====================================
SEKCJA:slotmachine
====================================
'''
# import random
#
# def spin_row():
#     symbol = ["🍒", '🍋', '🍊', '🍉', '🍇', "🍀"]
#     return [random.choice(symbol) for _ in range(3)]
#
#
# def print_row(row):
#     print('_________')
#     print("|".join(row))
#     print('_________')
#
#
# def get_peyout(row,bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == "🍒":
#             return bet * 3
#         elif row[0] == '🍋':
#             return bet * 4
#         elif row[0] == '🍊':
#             return bet * 5
#         elif row[0] == '🍉':
#             return bet * 10
#         elif row[0] == '🍇':
#             return bet * 2
#         elif row[0] == "🍀":
#             return bet * 100
#     return 0
#
#
#
# def main():
#     balans = 100
#     print("===================================")
#     print("witamy w kasynie")
#     print("symbole: 🍒, 🍋, 🍊, 🍉, 🍇, 🍀")
#     print("===================================")
#
#     while balans > 0:
#         print(f"Aktualny balans: {balans}")
#
#         bet = input("Podaj stawke: ")
#         if not bet.isdigit():
#             print("Niepoprawna stawka. Podaj liczbe.")
#             continue
#
#         bet = int(bet)
#
#         if bet > balans:
#             print("Nie masz wystarczająco pieniędzy.")
#             continue
#         if bet <= 0:
#             print("Stawka musi być większa od 0.")
#             continue
#         balans -= bet
#
#         row = spin_row()
#         print("spining...\n")
#         print_row(row)
#
#         peyout = get_peyout(row,bet)
#
#         if peyout > 0:
#             print(f"Wygrales {peyout}")
#         else:
#             print("Niestety przegrales")
#         balans += peyout
#
#         play_again = input("Czy chcesz zagrac ponownie? (t/n): ").lower()
#
#         if play_again != "t":
#             break
#     print(f"Twoj balans to: {balans}")
#
# if __name__ == "__main__":
#     main()
'''0
====================================
SEKCJA:Program szyfrowania
====================================
'''
# import random
# import string
#
# znaki = " "+string.punctuation + string.digits + string.ascii_letters +"ł" + "ó" + "ó" + "ą" + "ę" + "ś" + "ć" + "ń" + "ź" + "ż"
#
# znaki = list(znaki)
# klucz = znaki.copy()
# random.shuffle(klucz)
#
# print(f'znaki: {znaki}')
# print(f'klawisz: {klucz}')
#
# #szyfrowanie
# twoj_tekst= input("podaj tekst do szyfrowania: ")
# zaszyfrowany_tekst = ""
#
# for litera in twoj_tekst:
#     index = znaki.index(litera)
#     zaszyfrowany_tekst += klucz[index]
# print(f"Twoj tekst: {twoj_tekst}")
# print(f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")
'''
====================================
SEKCJA:nauka samodzielna
====================================
'''
# def oblicz_srednia(lista_liczb):
#     suma = sum(lista_liczb)
#     srednia = suma / len(lista_liczb)
#     return round(srednia,2)
# def main():
#     dane = input("Wpisz liczby do obliczenia sredniej. Odzielonymi przecinkami: ")
#     liczby = dane.split(",")
#     lista_liczb = list(map(float, liczby))
#
#     wynik = oblicz_srednia(lista_liczb)
#     print(wynik)
#
# if __name__ == "__main__":
#     main()
# def litery_w_tekście(tekst):
#     litery = tekst.lower()
#     licznik = {}
#     for litera in litery:
#         if litera in licznik:
#             licznik[litera] += 1
#         else:
#             licznik[litera] = 1
#     return licznik
#
#
# def main():
#     tekst = input("Wpisz cokolwiek:")
#     wynik = litery_w_tekście(tekst)
#     for litera in wynik.items():
#         print(f"{litera[0]}: {litera[1]}")
#
# if __name__ == '__main__':
#     main()

'''
====================================
SEKCJA:hangman 
====================================
'''
# import random
#
# words = ("apple", "banana", "orange", "grape", "kiwi", "watermelon")
#
# hangman_art = {
#     0: (" ", " ", " "),
#     1: (" o", " ", " "),
#     2: (" o", "|", " "),
#     3: (" o", "/|", " "),
#     4: (" o", "/|\\", " "),
#     5: (" o", "/|\\", "/ "),
#     6: (" o", "/|\\", "/ \\"),
# }
#
# def display_man(wrong_guesses):
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#
# def display_hint(hint):
#     print(" ".join(hint))
#
# def main():
#     answer = random.choice(words)
#     hint = list("_" * len(answer))
#     wrong_guesses = 0
#     guessed_letters = set()
#     wlaczone = True
#
#     while wlaczone:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Zgadnij literę: ").lower()
#
#         if guess in guessed_letters:
#             print("Już próbowałeś tej litery.")
#             continue
#
#         guessed_letters.add(guess)
#
#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             print("Nie ma takiej litery!")
#             wrong_guesses += 1
#
#         if "_" not in hint:
#             display_hint(hint)
#             print("Gratulacje! Odgadłeś hasło:", answer)
#             wlaczone = False
#         elif wrong_guesses >= 6:
#             display_man(wrong_guesses)
#             print("Przegrałeś! Prawidłowe hasło to:", answer)
#             wlaczone = False
#
# if __name__ == "__main__":
#     main()
'''
====================================
SEKCJA:programowanie obiektowe
====================================
'''
'''
🧱 Obiekt (object)
Obiekt to taki „pakiet” (z ang. bundle) zawierający:

atrybuty (czyli zmienne — opisujące cechy),

metody (czyli funkcje — opisujące działania).

📦 Przykłady obiektów: telefon, kubek, książka.
Każdy z nich ma swoje cechy (np. kolor, waga) i może coś robić (np. dzwonić, nalewać kawę, otwierać się).

🧰 Klasa (class)
Klasa to jak szablon albo projekt, który opisuje, jak taki obiekt ma wyglądać i działać.
Dzięki klasie możesz tworzyć wiele obiektów tego samego typu, ale z różnymi danymi.

🧾 Przykład:
Masz klasę Telefon, a z niej tworzysz obiekt mój_telefon i twój_telefon.
'''
# from cars import car
# car1 = car("BMW","2025","czerowny",True)
# car2 = car("Dodge","2023","czarny",False)
#
# car1.drive()
# car1.stop()

'''
🔹 Zmienne klasowe
 Zmienne klasowe to takie zmienne, które są wspólne dla wszystkich obiektów (czyli tzw. instancji) danej klasy.
Każda instancja ma dostęp do tych zmiennych, ale nie może ich zmieniać.
🔹 Zmienne instancji
Zmienne instancji to takie zmienne, które są unikalne dla każdej instancji danej klasy.
Każda instancja ma swoje własne zmienne, które mogą mieć różne wartości.
'''
# class uczen:
#
#     class_year = 2025
#     ilosc_uczniow = 0
#
#     def __init__(self,imie,wiek):
#         self.imie = imie
#         self.wiek = wiek
#         uczen.ilosc_uczniow += 1
#
#
# uczen1 = uczen("Michał", 17)
# uczen2 = uczen("Ola", 18)
# uczen3 = uczen("Kuba", 19)
# uczen4 = uczen("Franek", 22)
#
#
#
# print(f"Ostatni rok mojej klasy to: {uczen.class_year} z  {uczen.ilosc_uczniow} uczniami")
# print(uczen1.imie)
# print(uczen2.imie)
# print(uczen3.imie)
# print(uczen4.imie)
'''
1. Inheritance = Allows a class to inherit attributes and methods from another class
👉 Dziedziczenie pozwala jednej klasie przejąć (odziedziczyć) właściwości (atrybuty) i funkcje (metody) z innej klasy.
Czyli nowa klasa nie musi wszystkiego pisać od nowa – może korzystać z kodu innej klasy.    
To pomaga w ponownym użyciu kodu i łatwym jego rozszerzaniu.
Zamiast kopiować ten sam kod kilka razy, tworzysz "rodzica" (Parent), a potem robisz "dziecko" (Child), które go dziedziczy.
👉 Tak zapisuje się dziedziczenie w Pythonie:
Tworzysz klasę Child, która dziedziczy po klasie Parent.
# '''
# class zwierzeta:
#     def __init__(self, imie):
#         self.imie = imie
#         self.zyje = True
#
#     def eat(self):
#         print(f"{self.imie} je")
#     def sleep(self):
#         print(f"{self.imie} nie spi")
#
# class dog(zwierzeta):
#     def speak(self):
#         print("hau hau")
# class cat(zwierzeta):
#     def speak(self):
#         print("miau miau")
# class mouse(zwierzeta):
#     def speak(self):
#         print("pipi pipi")
#
# dog = dog("Scooby")
# cat = cat("Mruczek")
# mouse = mouse("szczurek")
# print(dog.imie)
# print(dog.zyje)
# dog.eat()
# dog.sleep()
'''
multiple dziedziczenie = to sytuacja, w której klasa dziedziczy po więcej niż jednym rodzicu.
C(A,B)
multilevel dziedziczenie = to sytuacja, w której klasa dziedziczy po innej klasie, która sama dziedziczy po innej klasie.
'''
# class zwierzeta:
#     def __init__(self,imie):
#         self.imie = imie
#
#     def eat(self):
#         print(f" {self.imie} je")
#     def sleep(self):
#         print(f" {self.imie}  spi")
#
#
# class ofiara(zwierzeta):
#     def ucieczka(self):
#         print(f"{self.imie}  ucieka")
#
# class drapieznik(zwierzeta):
#     def atak(self):
#         print(f"{self.imie} atakuje")
#
# class krolik(ofiara):
#     pass
#
# class orzel(drapieznik):
#     pass
#
# class ryba(ofiara,drapieznik):
#     pass
#
# krolik = krolik("Krolik")
# orzel = orzel("orzel")
# ryba = ryba("cwel")
#
# ryba.atak()
'''
====================================
SEKCJA: super()
====================================
Funkcja używana w klasie dziecka (child class), żeby wywołać metody z klasy rodzica (super class)
Pozwala rozszerzyć działanie odziedziczonej metody.
'''
# class kształt:
#     def __init__(self, kolor, is_wypełniony):
#         self.kolor = kolor
#         self.is_wypełniony = is_wypełniony
#     def opisz(self):
#         print(f"To jest kolor { self.kolor} i {'wypełniony' if self.is_wypełniony else 'nie wypełniony'}")
#
#
#
# class koło(kształt):
#     def __init__(self,kolor,is_wypełniony,promien):
#         super().__init__(kolor,is_wypełniony)
#         self.promien = promien
#     def opisz(self):
#         print(f"Obwód tego koła to : {3,14 * self.promien ** 2:.1f}cm^2 ")
#         super().opisz()
#
#
#
# class kwadrat(kształt):
#     def __init__(self,kolor,is_wypełniony,szerokosc):
#         super().__init__(kolor, is_wypełniony)
#         self.szerokosc = szerokosc
#
#     def opisz(self):
#         print(f"Obwód tego kwadratu to : {self.szerokosc * self.szerokosc:.1f}cm^2 ")
#         super().opisz()
#
#
#
# class trojkat(kształt):
#     def __init__(self,kolor,is_wypełniony,wysokosc,szerokosc):
#         super().__init__(kolor, is_wypełniony)
#         self.wysokosc = wysokosc
#         self.szerokosc = szerokosc
#     def opisz(self):
#         print(f"Obwód tego trojkata to : {self.szerokosc * self.wysokosc /2 :.1f}cm^2 ")
#         super().opisz()
#
#
# koło = koło("czerwony",True,5)
# kwadrat = kwadrat("zielony",False,10)
# trojkat = trojkat("niebieski",True,5,10)
#
#
# trojkat.opisz()
# class pracownik():
#     def __init__(self,imie,nazwisko,firma):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.firma = firma
#     def przedstawsie(self):
#         print(f"Imie: {self.imie}")
#         print(f"Nazwisko: {self.nazwisko}")
#         print(f"Firma: {self.firma}")
#
#
# class programista(pracownik):
#     def __init__(self,imie,nazwisko,firma,jezyk):
#         super().__init__(imie,nazwisko,firma)
#         self.jezyk = jezyk
#     def przedstawsie(self):
#         super().przedstawsie()
#         print(f"Język programowania: {self.jezyk}")
#         print("Programista")
#
# class sprzedawca(pracownik):
#     def __init__(self,imie,nazwisko,firma,region):
#         super().__init__(imie,nazwisko,firma)
#         self.region = region
#     def przedstawsie(self):
#         super().przedstawsie()
#         print(f"Sprzedaje pączki w : {self.region}")
#         print("Sprzedawca")
#
# programista = programista("Michał","Kowalski","Google","Python")
# programista.przedstawsie()
'''
=====================================
SEKCJA:polimorfizm
=====================================
olimorfizm oznacza, że różne obiekty mogą zachowywać się podobnie, mimo że są różne.

Inaczej mówiąc: jedna nazwa – różne zachowania.
'''
# from abc import ABC, abstractmethod
# class kształt:
#
#     @abstractmethod
#     def obwod(self):
#         pass
#
# class koło(kształt):
#     def __init__(self, promien):
#         self.promien = promien
#
#     def obwod(self):
#         return 3.14 * self.promien ** 2
#
# class kwadrat(kształt):
#     def __init__(self, strona):
#         self.strona = strona
#
#     def obwod(self):
#         return self.strona * self.strona
#
# class trojkat(kształt):
#     def __init__(self, wysokosc,podstawa):
#         self.wysokosc = wysokosc
#         self.podstawa = podstawa
#
#
#     def obwod(self):
#         return self.podstawa * self.wysokosc * 0.5
# class Pizza(koło):
#     def __init__(self,topping,promien):
#         super().__init__(promien)
#         self.topping = topping
#
#
#
#
#
# kształty = [koło(4), kwadrat(5), trojkat(6,7),Pizza("peperoni",15)]
#
# for kształt in kształty:
#     print(f"{kształt.obwod()} cm²")
'''
=====================================
SEKCJA:duck typing
=====================================
🔹 Duck typing = "Nie ważne czym jesteś, ważne co potrafisz"
🔹 Python patrzy, czy obiekt ma potrzebne metody, a nie jakiego jest typu
🔹 Pozwala pisać elastyczny i prosty kod
🔹 Typowe w językach dynamicznych, jak Python
'''

# class animal():
#     alive = True
#
# class dog(animal):
#     def speak(self):
#         print("hau hau")
#
# class cat(animal):
#     def speak(self):
#         print("miau miau")
#
# class car:
#     alive = True
#
#     def speak(self):
#         print("beep beep")
#
#
# animals = [dog(), cat(),car()]
# for animal in animals:
#     animal.speak()
#     print(f"{animal.alive}")
'''
=====================================
zadania
=====================================
'''
# class zwierzeta():
#     robi_dzwiek = True
#
# class krokodyl(zwierzeta):
#     def dzwiek(self):
#         print ("grr grr ")
# class zakso(zwierzeta):
#     def dzwiek(self):
#         print("Jestem zjebany,jestem zjebany")
#
# # osobna klasa
# class auta():
#     robi_dzwiek = True
# class dodge(auta):
#     def dzwiek(self):
#         print("WWWRRR BUM BUM WWWWRRRRR ")
# class tesla(auta):
#     def dzwiek(self):
#         print("sii sii")
#
# def zrob_dzwiek(obiekt):
#     obiekt.dzwiek()
#
# dodge = dodge()
# tesla = tesla()
# krokodyl = krokodyl()
# zakso = zakso()
#
# print (f" Ta dojebana fura (dodge) robi {zrob_dzwiek(dodge)}")
# zrob_dzwiek(tesla)
# zrob_dzwiek(krokodyl)
# zrob_dzwiek(zakso)

# kocham zycie !
# class zwierzeta():
#     def __init__(self, imie):
#         self.imie = imie
#
#     def dzwiek(self):
#         pass
# class pies(zwierzeta):
#     def dzwiek(self):
#         print(f"{self.imie} szczeka: Hau Hau")
# class kot(zwierzeta):
#     def dzwiek(self):
#         print(f"{self.imie} miauczy: Miau Miau")
# class krowa(zwierzeta):
#     def dzwiek(self):
#         print(f"{self.imie} muczy: Muu Muu")
# class owca(zwierzeta):
#     def dzwiek(self):
#         print(f"{self.imie} beczy: Beee Beee")
#
# class osoba:
#     def __init__(self,imie):
#         self.imie = imie
# # str wywoluje czytelny tekst zamist  czegos takiego: <__main__.Osoba object at 0x00000123ABCDEF>
#     def __str__(self):
#         return f"Osoba: {self.imie}"
# os = osoba("Jan")
# print(os)
'''
=====================================
Static methods
=====================================
 zwykła funkcja, która mieszka w klasie, ale nie obchodzi jej żaden obiekt tej klasy.

Nie potrzebuje self, nie interesuje się żadnymi danymi zapisanymi w obiekcie, nie korzysta też z cls 
(czyli z samej klasy). Po prostu jest zapisana w klasie, żeby było logicznie, gdzie powinna być, ale działa niezależnie od niej.
to taka ogolna wiedza, która nie jest związana z żadnym konkretnym obiektem.
'''
# class pracownik():
#     def __init__(self,imie,stopien):
#         self.imie = imie
#         self.stopien = stopien
#
#     def get_info(self):
#         return f"imie:{self.imie}, stopien: {self.stopien}"
#
#     @staticmethod
#     def jest_wazny(stopien):
#         wazne_stopnie = ["Manager","CEO","Szef kuchni"]
#         return stopien in wazne_stopnie
#
# pracownik1 = pracownik("Patryk","Manager")
# pracownik2 = pracownik("Dawid","Szef kuchni")
#
# print(pracownik.jest_wazny("CEO"))
# print(pracownik1.get_info())
# print(pracownik2.get_info())

# class Pociag:
#     def __init__(self,numer_p,typ_p):
#         self.numer_p = numer_p
#         self.typ_p = typ_p
#
#     def pokaz_info(self):
#         return f"Numer Pociagu:{self.numer_p}| Typ pociagu{self.typ_p}"
#     @staticmethod
#     def czy_pociag_szybki(typ_p):
#         szybkie_typy = ["Pendolino", "Express"]
#         return typ_p in szybkie_typy
#     def __str__(self):
#         return f"pociag o numerze {self.numer_p} i typie {self.typ_p}"
#
#
# pociag1 = Pociag("ab134","Pendolino")
# pociag2 = Pociag("ab1344","Pendolino")
# pociag3 = Pociag("a3fcd","bullet train")
#
# print(pociag1.czy_pociag_szybki("Pendolino"))
# print(pociag1)
# class samochod:
#     def __init__(self,marka,rocznik):
#         self.marka = marka
#         self.rocznik = rocznik
#     def pokaz_info(self):
#         return F"Marka: {self.marka}, Rocznik: {self.rocznik}"
#
#
#     def __str__(self):
#         return f"Samochod marki {self.marka}({self.rocznik})"
#
#
#     @staticmethod
#     def czy_klasyk(rocznik):
#         return 2025 - rocznik >= 30
#
# samochod1 = samochod("BMW", 2020)
# samochod2 = samochod("Polonez",1985)
#
# print(samochod1)
# print(samochod1.czy_klasyk(2020))
# print(samochod2.czy_klasyk(1985))
'''
=====================================
Class Methods
=====================================
metoda, która działa na samej klasie, a nie na konkretnym obiekcie.
Nie interesuje jej self (czyli konkretna instancja/obiekt), tylko cls – cała klasa.
'''
# class Student:
#     #parametry klasy
#     liczba = 0
#     total_wiek = 0
#     #konstruktor klasy
#     def __init__(self,imie,wiek):
#         self.imie = imie
#         self.wiek = wiek
#         Student.liczba += 1
#         Student.total_wiek += wiek
#
#     #instant method
#     def daj_info(self):
#         return f"{self.imie} {self.wiek}"
#     #liczenie studentow
#     @classmethod
#     def zlicz_liczbe(cls):
#         return F"całkowita liczba studentow to: {cls.liczba}"
#
#     # #liczenie sredniego wieku studentow
#     @classmethod
#     def sredni_wiek(cls):
#         if cls.liczba == 0:
#             return "Brak studentów"
#         return f"Sredni wiek studentow to: {cls.total_wiek / cls.liczba:.2f} lat"
#
# # przypisanie i uzycie
# s1 = Student("Michał", 17)
# s2 = Student("Michał", 100)
# s3 = Student("Michał", 65)
# s4 = Student("Michał", 3)
#
# print(Student.zlicz_liczbe())
# print(Student.sredni_wiek())
'''
=====================================
magic methods
=====================================
Są automatycznie wywoływane przez Pythona, gdy wykonujesz różne wbudowane operacje – np. tworzysz obiekt, porównujesz, drukujesz, dodajesz itd.
Pozwalają programiście zdefiniować lub zmienić zachowanie obiektów – np. jak się wyświetlają, jak się dodają, jak się porównują.
'''
# class book:
#
#
#     # konstruktor klasy
#     def __init__(self,tytul,autor,ilosc_stron):
#         self.tytul = tytul
#         self.autor = autor
#         self.ilosc_stron = ilosc_stron
#
#     def __str__(self):
#         return f"Tytuł:{self.tytul},autor:{self.autor}, ilość stron:{self.ilosc_stron}"
#
#     def __eq__(self,other):
#         return self.tytul == other.tytul and self.autor == other.autor
#
#     def __lt__(self,other):
#         return self.ilosc_stron > other.ilosc_stron
#
#     def __add__(self,other):
#         return f"łącznie stron: {self.ilosc_stron + other.ilosc_stron}"
#
#     def __contains__(self,keyword):
#         return keyword in self.tytul or keyword in self.autor
#
#     def __getitem__(self,key):
#         if key == "title":
#             return self.tytul
#         elif key == "autor":
#             return self.autor
#         elif key == "ilosc_stron":
#             return self.ilosc_stron
#         else:
#             return f"nie znaleziono klucza: {key}"
#
# book1= book("hobbit","Tolkien",310)
# book2 = book("Harry Potter","JK. Rowling",223)
# book3 = book("Potop","sienkiewicz",333)
#
#
# print(book3['title'])
# print(book3['audio'])
#
# # print(book3)
# # print(book1 == book2)
# # print(book1 < book3)
# # print(book1 > book3)
# # print(book1 + book3)
# # print("Potop" in book3)
# # print("Harry" in book3)
'''
=====================================
@property
=====================================
To dekorator w Pythonie, który zamienia metodę w „zwykły atrybut”.
Dzięki temu możesz wywołać funkcję bez nawiasów (), jakby to była zwykła zmienna.

w skrocie: nie musisz używać nawiasów, żeby uzyskać wartość z metody.
'''
#
# class Prostokąt:
#     def __init__(self,szerokosc,wysokosc):
#         self._szerokosc = szerokosc
#         self._wysokosc = wysokosc
#     #property do pobierania wartosci
#     @property
#     def szerokosc(self):
#         return f'{self._szerokosc:.1f}cm'
#
#     @property
#     def wysokosc(self):
#         return f'{self._wysokosc:.1f}cm'
#     #settery do ustawiania nowych wartosci
#     @szerokosc.setter
#     def szerokosc(self, nowa_szerokosc):
#         if nowa_szerokosc > 0:
#             self._szerokosc = nowa_szerokosc
#         else:
#             raise ValueError("Szerokość musi być większa od zera")
#
#     @wysokosc.setter
#     def wysokosc(self, nowa_wysokosc):
#         if  nowa_wysokosc > 0:
#             self._wysokosc = nowa_wysokosc
#         else:
#             raise ValueError("Wysokosc musi być większa od zera")
#     #delete aby usuwac
#     @szerokosc.deleter
#     def szerokosc(self):
#         del self._szerokosc
#         print("Szerokosc bedzie usunieta")
#
#     @wysokosc.deleter
#     def wysokosc(self):
#         del self._wysokosc
#         print("wysokosc bedzie usunieta")
#
#
# prostokąt = Prostokąt(3,4)
#
# prostokąt.szerokosc = 5
# #prostokąt.szerokosc = 0  # To spowoduje błąd, ponieważ szerokość musi być większa od zera
#
# del prostokąt.szerokosc
# del prostokąt.wysokosc
'''
=====================================
decoratory
=====================================
Dekorator to funkcja, która dodaje coś do innej funkcji, bez zmieniania jej kodu.
Oryginalna funkcja przekazywana jest jako argument do dekoratora
'''
#
# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("Dodałes posypke")
#         func(*args, **kwargs)
#     return wrapper
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("dodales fudge🍫")
#         func(*args, **kwargs)
#     return wrapper
#
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Oto twoje {flavor} lody🍧")
#
# get_ice_cream("wanilliowe ")
'''
=====================================
exceptions (wyjątki)
=====================================
Wyjątki to błędy, które pojawiają się podczas działania programu.
Np. gdy Python próbuje coś zrobić, ale coś idzie nie tak — np. dzielenie przez zero, brak pliku, czy błąd w nazwie zmiennej.
'''
'''
=====================================
try-except
=====================================
Wyjątki to błędy, które pojawiają się podczas działania programu.

Np. gdy Python próbuje coś zrobić, ale coś idzie nie tak — np. dzielenie przez zero, brak pliku, czy błąd w nazwie zmiennej.

3 kroki:
try: Tutaj piszesz kod, który może wywołać wyjątek.
except: Tutaj piszesz, co ma się stać, gdy wyjątek wystąpi.
finally: (opcjonalne) Tutaj możesz napisać kod, który zawsze się wykona, niezależnie od tego, czy wyjątek wystąpił, czy nie.
'''
# try:
#     num = int(input("Podaj liczbę: "))
#     print(1 / num)
# except ZeroDivisionError:
#     print("Nie można dzielić przez zero!")
# except ValueError:
#     print("to nie liczba!")
# except Exception:
#     print("Wystąpił nieoczekiwany błąd!")
# finally:
#     print("koniec")
# try:
#     num = int(input("Podaj liczbe:"))
#     print(1 / num)
# except ZeroDivisionError as e:
#     print(f"Nie można dzielić przez zero! Błąd: {e}")
# except ValueError as e:
#     print(f"To nie jest liczba! Błąd: {e}")
# except Exception as e:
#     print(f"Wystąpił nieoczekiwany błąd! Błąd: {e}")
'''
=====================================
Python file detection
=====================================
Ten program służy do wykrywania plików w Pythonie
'''
# import os
# file_path = "C:\\Users\\user\\Desktop"
#
# if os.path.exists(file_path):
#     print(f"Lokalizacja pliku: {file_path} istnieje.")
#     if os.path.isfile(file_path):
#         print("To jest plik.")
#     elif os.path.isdir(file_path):
#         print("to jest folder")
# else:
#     print(f"Lokalizacja pliku: {file_path} nie istnieje.")
#
# powtorzenie
#
# import os
#
# file_path = "C:\\Users\\user\\Desktop\\test"
# if os.path.exists(file_path):
#     print(f"Plik istnieje,a jego sciezka to: {file_path}")
#     if os.path.isfile(file_path):
#         print("To jest plik.")
#     elif os.path.isdir(file_path):
#         print("To jest folder.")
# else:
#     print(f"Plik nie istnieje!")
'''
=====================================
phyton write file(.txt, .csv, .json)
=====================================
    |mode – najczęściej używane tryby:
    |mode	Znaczenie	Opis działania
    
"r"	    read (czytaj)	Domyślny tryb – otwiera plik do czytania. Błąd, jeśli plik nie istnieje.
"w"	    write (pisz)	Tworzy nowy plik lub nadpisuje istniejący!
"a"	    append (dopisz)	Dodaje dane na końcu pliku (nie kasuje istniejących).
"x"	    create (stwórz nowy)	Tworzy nowy plik. Błąd, jeśli już istnieje.
"b"	    binary (binarny)	Dodajesz do innych trybów, np. "rb" albo "wb" dla plików binarnych (np. zdjęć).
"+"	    read + write (czytaj + pisz)	Dodajesz do innych trybów: "r+", "w+", "a+".
'''
# import json
# import csv
#
# tworzenie pliku csv

# pracownicy =[["Imie","wiek","praca"],
#              ["Michał",30,"Szlachcic"],
#              ["Jarema",35,"Wojewoda Ruski"],
#              ["Jan Kazimierz",27,"Król Rzeczypospolitej Polski"],]
#
# file_path = "C:/Users/user/Desktop/output.csv"
# try:
#     with open(file=file_path, mode="w") as file:
#         writer = csv.writer(file)
#         for row in pracownicy:
#             writer.writerow(row)
#         print(f"plik csv '{file_path}' zostal stworzony ")
# except FileExistsError:
#     print("ten plik juz istnieje")


# tworzenie pliku json
# import json
#
# pracownicy_json = {
#     "pracownicy": [
#         {"imie": "Michał", "wiek": 30, "praca": "Szlachcic"},
#         {"imie": "Jarema", "wiek": 35, "praca": "Wojewoda Ruski"},
#         {"imie": "Jan Kazimierz", "wiek": 27, "praca": "Król Rzeczypospolitej Polski"}
#     ]
# }
# file_path_json = 'C:\\Users\\user\\Desktop\\output.json'
# try:
#     with open(file_path_json, mode="w") as file:
#         json.dump(pracownicy_json, file,indent=4)
#         print(f"plik json '{file_path_json}' zostal stworzony ")
# except FileExistsError:
#     print("ten plik json juz istnieje")
#
#
# pracownicy_txt = {
#     "Spangebob"
# }
#
# file_path_txt = "C:\\Users\\user\\Desktop\\output.txt"
# try:
#     with open(file_path_txt,mode="w")as file:
#         for pracownik_txt in pracownicy_txt:
#             file.write(f"{pracownik_txt}\n")
#         print("Plik tekstowy zostal stworzony")
# except FileNotFoundError:
#     print("plik zostal juz stworzony")


'''
=====================================
phyton read file(.txt, .csv, .json)
=====================================
'''
# file_path = "C:\\Users\\user\\Desktop\\output.txt"
# try:
#     with open(file_path, mode="r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Ten plik nie zostal znaleziony")
# except PermissionError:
#     print("nie masz uprawnień do odczytu pliku")


# import json
# file_path = "C:\\Users\\user\\Desktop\\output.json"
# try:
#     with open(file_path, mode="r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("Ten plik nie zostal znaleziony")
# except PermissionError:
#     print("nie masz uprawnień do odczytu pliku")

# import csv
# file_path = "C:\\Users\\user\\Desktop\\output.csv"
# try:
#     with open(file_path, mode="r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
#         print(content)
# except FileNotFoundError:
#     print("Ten plik nie zostal znaleziony")
# except PermissionError:
#     print("nie masz uprawnień do odczytu pliku")
'''
=====================================
Daty i czas
=====================================
'''
import datetime
#
# data = datetime.date(2025,6,6)
# dzisiaj = datetime.date.today()
#
# time = datetime.time(13,21,)
# now = datetime.datetime.now()
#
# now = now.strftime("%H:%M:%S \n%d.%M.%y")
#
# target_datetime = datetime.datetime(2025,1,1,12,0,0)
# current_datetime = datetime.datetime.now()
# if target_datetime < current_datetime:
#     print("Czas docelowy jest w przeszłości")
# else:
#     print("Czas docelowy jest w przyszłości")
'''
=====================================
Zegarek
=====================================
'''
import time
import datetime
import pygame
#
# def set_alarm(czas_zegarka):
#     print(f"Alarm ustawiono na {czas_zegarka}.")
#     sound_file = "gta-v-notification.mp3"
#     _działa = True
#     while _działa:
#         obecny_czas = datetime.datetime.now().strftime("%H:%M:%S")
#         print(obecny_czas)
#         if obecny_czas == czas_zegarka:
#             print("wstawaj gnoju")
#
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play(loops=4)
#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#
#             _działa = False
#
#         time.sleep(1)
#
# if __name__ == "__main__":
#     czas_zegarka = input("Podaj czas alaramu (HH:MM:SS): ")
#     set_alarm(czas_zegarka)
help(time)
'''
=====================================
multithreading
=====================================
Uzywane do wykonywania wielu zadan w tym samym czasie
dobre do Input/output
threading(Thread)(target=my_function, args=(arg1, arg2))
'''
# import threading
# import time
#
#
# def walk_dog(imie_psa,):
#     time.sleep(8)
#     print (f"skonczyles wyprowadzanie {imie_psa}")
# def wyrzucanie_smieci():
#     time.sleep(2)
#     print("wyrzuciles smieci")
# def nadanie_listu():
#     time.sleep(4)
#     print("nadales list")
# #nici=thread
# nić1 = threading.Thread(target=walk_dog, args=("Lili",))
# nić1.start()
#
# nić2 = threading.Thread(target=wyrzucanie_smieci)
# nić2.start()
#
# nić3 = threading.Thread(target=nadanie_listu)
# nić3.start()
# # join aby czekać na zakończenie wątków
# nić1.join()
# nić2.join()
# nić3.join()
#
# print("Wszystkie obowiazki Wykonane!")
'''
====================================
Jak połaczyc API uzywajac Pythona
====================================
'''
# import requests
#
# podstawowy_url = "https://pokeapi.co/api/v2/"
#
# def get_pokemon_inf(imie):
#     url = f"{podstawowy_url}/pokemon/{imie}"
#     odpowiedz = requests.get(url)
#     #print(odpowiedz)
#
#     if odpowiedz.status_code == 200:
#         pokemon_data = odpowiedz.json()
#         return pokemon_data
#     else:
#         print(f"nie znaleziono informacji,ERROR {odpowiedz.status_code}")
#
# pokemon_name = "gengar"
# pokemon_info = get_pokemon_inf(pokemon_name)
#
# if pokemon_info:
#     print(f"Imie: {pokemon_info['name'].capitalize()}")
#     print(f"id: {pokemon_info['id']}")
#     print(f"Wysokosc: {pokemon_info['height']}")
#     print(f"Waga: {pokemon_info['weight']}")
#
'''
====================================
Pierwsze gui
====================================
PyQt5 !!
# '''
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Moja pierwsze gui") # Ustawia tytuł okna
#         #self.setGeometry(x,y,width,height)
#         self.setGeometry(700,300,500,500) # Ustawia pozycję i rozmiar okna
#         self.setWindowIcon(QIcon("Lottery_Slots.png")) # Ustawia ikonę okna
#
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     main()
#







# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Moja pierwsze gui") # Ustawia tytuł okna
#         #self.setGeometry(x,y,width,height)
#         self.setGeometry(700,300,500,500) # Ustawia pozycję i rozmiar okna
#         self.setWindowIcon(QIcon("Lottery_Slots.png")) # Ustawia ikonę okna
#
#         label = QLabel("Hello",self)
#         label.setFont(QFont("Arial",40))  # Ustawia czcionkę etykiety
#         label.setGeometry(0,0,500,100)  # Ustawia wyrównanie etykiety do środka
#         label.setStyleSheet("color: #4d0f25;"
#                             "background-color: #736d6f;"
#                             "font-style: italic;"
#                             "font-weight: bold;"
#                             "text-decoration: underline")
#         # label.setAlignment(Qt.AlignTop) # Ustawia wyrównanie do góry
#         # label.setAlignment(Qt.AlignVCenter)  # Ustawia wyrównanie do środka
#         # label.setAlignment(Qt.AlignBottom) #ustawia na dole
#         # label.setAlignment(Qt.AlignRight) #ustawia na dole
#         # label.setAlignment(Qt.AlignHCenter) #ustawia na srodek
#         # label.setAlignment(Qt.AlignLeft) #ustawia na lewo
#
#
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)# srodek gora
#         #  label.setAlignment(Qt.AlignCenter)# srodek
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     main()
print("Hello World!")