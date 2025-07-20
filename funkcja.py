from unittest import case
# def parzyste_do_n(n):
#     parzyste = []
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             parzyste.append(i)
#     return parzyste
#
# print(f"Parzyste: {parzyste_do_n(10)}")
# def filtruj_liczby(n:int,typ:str) -> list[int]:
#     parzyste = []
#     nieparzyste = []
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             parzyste.append(i)
#         else:
#             nieparzyste.append(i)
#     match typ:
#         case "parzyste":
#             return parzyste
#         case "nieparzyste":
#             return nieparzyste
#         case _:
#             return []
# print(filtruj_liczby(1,"parzyste"))

# zadanie 1:
lista_slow = ["Michal","Grzegorz","Anna","konstantynopolitańczykowianeczka"]
def  najdluzszy_wyraz(lista_slow):
    najdluzszy = lista_slow[0]
    for slowo in lista_slow:
        if len(slowo) > len(najdluzszy):
            najdluzszy = slowo
    return najdluzszy
print(najdluzszy_wyraz(lista_slow))

