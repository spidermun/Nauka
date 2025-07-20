#zadanie 1
# for i in range(100,1,-5):
#     print(i)
#
#zadanie 2
#
# for i in range(4):
#     for j in range(4):
#         print("#", end="")
#     print()
#zadanie 3
#
# suma = 0
# for i in range(1,1000):
#     if i % 7 == 0:
#         suma += 1
# print(suma)
#zadanie 4
# lista = []
# for i in range(1,10):
#     if i % 2 == 0:
#         lista.append(i)
# print(lista)
# print(sum(lista))
# n= 10
# for i in range(1,n+1): # kolumny
#     # print(i)
#     for j in range(i,n+1): # wiersze
#         print(f"{i} x {j} = {i*j}")
# liczby = set()
# for i in range(1,100):
#     if i % 3 == 0:
#         if not i % 5 == 0:
#             liczby.add(i)
# print(liczby)
# n = 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# imiona = ["Ania", "Bartek", "Celina", "Darek", "Ewa"]
# for index in range(len(imiona)):
#     print(imiona[index])
#
# imiona = ["Ania", "Bartek", "Celina"]
# nazwiska = ["Kowalska", "Nowak", "Zielińska"]
#
# for index in range(len(imiona)):
#     print(imiona[index], nazwiska[index])
# uczniowie = ["Ania", "Bartek", "Celina"]
# oceny = [
#    [5, 4, 3],   # Ania
#    [2, 3, 4],   # Bartek
#    [4, 5, 5]    # Celina
# ]
# for index in range(len(uczniowie)):
#     print(uczniowie[index], oceny[index])
# n = 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(3):
#     for j in range(3):
#         print("x",end="")
#     print()

# a = 10
# b = 20
# for liczba in range(a,b+1):
#     if liczba % 2 == 0:
#         print(liczba)
#
# n = 4
# silnia = 1
# for liczba in range(1,n+1):
#     silnia *= liczba
# print(silnia)

# tekst = ["Ala ma kota"]
# for index in tekst:
#     print(index[::-1])

# liczba = 13
# ile_cyfr = 0
# if liczba == 0:
#     ile_cyfr += 1
# else:
#     while liczba != 0:
#         liczba //= 10
#         ile_cyfr += 1
# print(ile_cyfr)
"""
zagniezdzone
"""
from tokenize import endpats

# for wiersze in range(1,4+1):
#     for kolumny in range(1,7+1):
#         print("*",end=" ")
#     print()

# for wiersze in range(1,5+1):
#     for kolumny in range(wiersze):
#         print("*",end="")
#     print()

# n = 10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i * j, end="\t")
#     print()

# for x in range(1,8+1):
#     for o in range(1,8+1):
#         if (x + o) % 2 == 0:
#             print("X",end="")
#         else:
#             print("O",end="")
#     print()
# n = 4
# for i in range(n):  # dla każdego wiersza
#     for j in range(2 * n - 1):  # dla każdej kolumny
#         if n - i - 1 <= j <= n + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# #
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         y = x_str[::-1]
#         print(x)
#

"""
Go to the data folder and use the countries_data.py file.
1. What are the total number of languages in the data
2. Find the ten most spoken languages from the data
3. Find the 10 most populated countries in the world
"""
# from countries_data import COUNTRIES
# from collections import Counter
# #
# # # Zliczamy wystąpienia języków w krajach
# # language_count = Counter()
# # for country in COUNTRIES:
# #     for language in country["languages"]:
# #         language_count[language] += 1
# #
# # # Pobieramy 10 najczęściej występujących języków
# # top_10 = language_count.most_common(10)
# #
# # # Wyświetlamy wyniki
# # for lang, count in top_10:
# #     print(f"{lang}: {count}")
#
#
#
#
# # Lista tupli: (nazwa kraju, populacja)
# populacje = [(kraj["name"], kraj["population"]) for kraj in COUNTRIES]
# # Sortujemy po populacji malejąco
# populacje_sorted = sorted(populacje, key=lambda x: x[1], reverse=True)
# # Bierzemy top 10
# top_10 = populacje_sorted[:10]
# # wyswietlamy
# for nazwa, populacja in top_10:
#     print(f"{nazwa}: {populacja}")


# najwiecej = COUNTRIES[0]
# for country in COUNTRIES:
#     # print(f"{country['name']},{len(country['languages'])}")
#     if len(country['languages']) > len(najwiecej):
#         najwiecej = country
# print(f"{najwiecej['name']},{len(najwiecej['languages'])}")

# suma_j = 0
# for i in range(len(COUNTRIES)):
#     total_languages = len((COUNTRIES[i]["languages"]))
#     for j in range(total_languages):
#         suma_j += 1
# print(f"Wszytkich jezykow łacznie jest: {suma_j}")


def fun():
    prices = [10,20,30]
    total = 0
    for price in prices:
        total += price
    return total

def fun1():
    numbers = [5,2,5,2,2]
    for num in numbers:
        output = ''
        for count in range(num):
            output += "x"
        print(output)
    return ""




def fun2(num1: int, num2: int) -> int:
    num3 = num1 + num2
    return num3


def najwieksza(lista):
    najwieksza = 0
    for num in lista:
        if num > najwieksza:
            najwieksza = num
    return najwieksza

def czy_palindrom(lista):
    liczba = lista[0]
    x_str = str(liczba)
    y = x_str[::-1]
    if x_str == y:
        return True
    else:
        return False






# n = 20
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)



# lista = [1,1,1,1,1,1]
#
# print(dir(list))
#
#
# print(lista.remove(1))
# print(lista)

# liczba = 0
# n = 4
# for wiersz in range(1,n+1):
#     for kolumna in range(wiersz):
#         liczba += 1
#         print(liczba,end=" ")
#     print()


liczba = 1234  # tutaj wpisz dowolną liczbę całkowitą
suma = 0
for cyfra in str(liczba):
    suma += int(cyfra)
    pass



owoce = ["Banan","Borówka","Truskawki","Mango"]

for i in range(len(owoce)):
    if i == 1:
        print(owoce[i])