# Napisz funkcję, która przyjmuje liczbę n i wypisuje wszystkie liczby parzyste od 1 do n.
#
# 📌 Cel: poćwicz for i warunki.

# def parzyste(n):
#     parzyste = []
#     n = int(input("podaj liczbe: "))
#     for i in range(1,n):
#         if i % 2 == 0:
#             parzyste.append(i)
#     return parzyste
#

# def liczba_znakow(s, znak):
#     suma = 0
#     for litera in s.lower():
#         if litera == znak:
#             suma += 1
#     return suma
# print(liczba_znakow("Ala ma kota", "a"))

# def odwroc_liste(lista):
#     lista = ["gruszka", "banan", "jablko"]
#     for i in range(len(lista) - 1, -1, -1):
#         print(lista[i])
#
# odwroc_liste()

# n = 5
# for i in range(1, n + 1):       # idziemy od 1 do n włącznie
#     for j in range(1, i + 1):   # wypisujemy liczby od 1 do i włącznie
#         print(j, end="")        # wypisujemy bez przejścia do nowej linii
#     print()                     # przejście do nowej linii po zakończeniu pętli wewnętrznej
#
# for i in range(1, n+1):       # <--- zewnętrzna pętla: która linijka
#     for j in range(i):        # <--- wewnętrzna: ile razy wypisać coś
#         print(i, end="")      # <--- wypisujemy 'i', czyli numer linii
#     print()                   # <--- przechodzimy do nowej linii
# n=6
# for i in range(1,n+1):
#     print("*" * i)
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i + 1):
#         print(j, end="")
#     print()
# n = int(input("podaj liczbe: "))
# parzyste = []
# nieparzyste = []
# for index in range(1,n+1):
#     if index % 2 == 0:
#         parzyste.append(index)
#     else:
#         nieparzyste.append(index)
#
# for i in parzyste:
#     print(i,end=" ")
# print()
# for j in nieparzyste:
#     print(j,end=" ")
# def liczenie():
#     tekst = input("Podaj zdanie: ")
#     samogloski = "aeiouy"
#     samoglosek = 0
#     spolglosek = 0
#
#
#     for i in tekst:
#         if i.isalpha():
#             if i in samogloski:
#                 samoglosek += 1
#             else:
#                 spolglosek += 1
#     print(f'samoglosek: {samoglosek}')
#     print(f"spolglosek: {spolglosek}")
# liczenie()
# import random
#
# print("zgadnij liczbe")
# liczba = random.randint(1,100)
# punkty = 0
# wlacznik = True
# while wlacznik:
#     print(liczba)
#     guess = int(input("Guess: "))
#     if guess == liczba:
#         punkty += 1
#         print(f"Zgadłeś! Punkty: {punkty}")
#         liczba = random.randint(1, 100)
#         if punkty == 6:
#             print("Brawo wygrales! ")
#             wlacznik = False
#     elif guess < liczba:
#         print("liczba jest za mała")
#     elif guess > liczba:
#         print("liczba jest za duza")
#     else:
#         print("Nie ma tego co wpisales proboj dalej!")
# owoce = {"jabłko": 4,
#          "banan": 7,
#          "gruszka": 2}
#
# for klucz,wartosc in owoce.items() :
#     print(klucz,wartosc)
#
# n = 10
# n = 10
# parzyste = []
# for i in range(1,n+1):
#     if i % 2 == 0:
#         parzyste.append(i)
# print(parzyste)