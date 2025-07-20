# while True:
#     try:
#         calkowita = int(input("Liczba calkowita: "))
#         calkowita2 = int(input("2 Liczba calkowita: "))
#         x = calkowita / calkowita2
#         print(float((x)))
#     except ZeroDivisionError:
#         print("Nie dziel przez zero idioto to moze spalic komputer! ")
#     except ValueError:
#         print("To jest liczba? nie wydaje mi sie!")
#     else:
#         print("no brawo udalo ci sie")
#         break
'''
zagniezdzone wyjatki
'''
# try:  # Poziom 1
#     coś ryzykownego
# except TypBledu1:
#     try:  # Poziom 2
#         coś dodatkowego, co też może się nie udać
#     except TypBledu2:
#         obsługa dodatkowego błędu

# print("podaj 2 liczby")
# while True:
#     try:
#         num_1 = int(input("liczba 1 "))
#         num_2 = int(input("liczba 2 "))
#         num_3 = num_1 / num_2
#     except ValueError:
#         print("Podaj liczbe")
#     except ZeroDivisionError:
#         print("Nie dziel przez zero")
#     else:
#         print(num_3)
#         break


