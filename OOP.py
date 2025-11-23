import time

from reportlab.graphics.charts.legends import TotalAnnotator
from ursina.prefabs.primitives import model_names

from listakontaktow import wyswietl_wszytko


# class Samochod():
#     def __init__(self,kolor,model):
#         self.model = model
#         self.kolor = kolor
#     def klakson(self):
#         print("PIIIP PIIP KURWA PIIIP")
#     def mruganie_swiatlami(self):
#         print("mrug mrug kurwa murg!")
#     def info_auto(self):
#         return (f"Model Auta to:{self.model}, o kolorze {self.kolor}. ")
#
# fiat = Samochod(kolor="czerwony",model=500)
# print(fiat.info_auto())
# class Samochod():
#     auta = []
#
#     def __init__(self,kolor,marka,rok_produkcji):
#         self.marka = marka
#         self.kolor = kolor
#         self.rok_produkcji = rok_produkcji
#         Samochod.auta.append(self)
#
#     def __str__(self):
#         return f"Jestem Autem {self.marka}"
#
#     def __repr__(self):
#         return  f"Auto: {self.marka}"
#
#     def wiek(self):
#         wiek = 2025 - self.rok_produkcji
#         return wiek
#
#     def pokaz_inf(self,):
#         return (f"Auto marki: {self.marka} z roku: {self.rok_produkcji} o kolorze: {self.kolor}, ma {self.wiek()} lat")
#
#     def jedz(self):
#         return "Brum brum jade"
#
#
#
# class Samochodelektryczny(Samochod):
#     def __init__(self, kolor, marka, rok_produkcji,bateria):
#         super().__init__(kolor, marka, rok_produkcji)
#         self.bateria = bateria
#
#     def stan_baterii(self):
#         if self.bateria >= 30:
#             return "Naladowana"
#         else:
#             return "Rozladowana"
#
#
#     def jedz(self):
#         if self.bateria >= 5:
#             return "Bzz Bzz bzz"
#         else:
#             return "I chuj nie jade nie mam baterii"
#
#
#     def pokaz_inf(self):
#         tekst_rodzic = super().pokaz_inf()
#         stan = self.stan_baterii()
#         return f"{tekst_rodzic}, Bateria: {self.bateria}% - {stan}"
#
#
#
#
# dodge = Samochod(marka="Dodge",kolor="Czerwony",rok_produkcji=2020)
# Tesla = Samochodelektryczny(marka="tesla", kolor="czarny", rok_produkcji=2024,bateria=50)
#
# for samochod in Samochod.auta:
#     print(samochod.jedz())


# class Task:
#     def __init__(self,nazwa,data):
#         self.nazwa = nazwa
#         self.data = data
#
# class TaskManager():
#     def __init__(self):
#         self.taski = []
#
#     def add_task(self,data,nazwa):
#         task = Task(data,nazwa)
#         self.taski.append(task)
#
#     def usun(self,nazwa):
#         task_ = False
#         for task in self.taski:
#             if task.nazwa == task.nazwa:
#                 self.taski.remove(task)
#                 task_ = True
#                 break
#         if not task_:
#             return "Nie ma zadania!"
#
#     def display_tasks(self):
#         if not self.taski:
#             return "Brak"
#         else:
#             return [task for task in self.taski]
#
#     def change_data(self,nazwa,nowy_termin):
#         task_istnieje = False
#         for task in self.taski:
#             if task.nazwa == nazwa:
#                 task.data = nowy_termin
#                 task_istnieje = True
#                 return f"Nowy termin {nowy_termin}"
#         if not task_istnieje:
#             return "Nie ma takiego tasku"
#
# Task1 = TaskManager()
# print(Task1.add_task("2025/05/06", "Poucz sie"))
# Task1.add_task("2025/06/06", "Umuj sie")
# Task1.display_tasks()
# Task1.change_data("Poucz sie","2023/06/06")
# Task1.display_tasks()
#
# class Ptak():
#     def __init__(self,imie):
#         self.__imie = imie
#
#     # @property
#     def imie(self):
#         return self.__imie
#
#
# class Matma():
#     @staticmethod
#     def dodawanie(a,b):
#         return a + b
# print(Matma.dodawanie(1,2))
# class Konto():
#     def __init__(self,numer_konta):
#         self._balance = 0
#         self._numer_konta = numer_konta
#
#
#     #Numer konta
#     @property
#     def numer_konta(self):
#         return self._numer_konta
#
#     @numer_konta.setter
#     def numer_konta(self,wartosc):
#         print( "Nie mozesz go modyfikowac")
#
#     @numer_konta.deleter
#     def numer_konta(self,wartosc):
#         print("nie mozesz go usunac")
#
#     # balans
#     @property
#     def balance(self):
#             return self._balance
#     @balance.setter
#     def balance(self, wartosc):
#         if wartosc < 0:
#             print("nie mozna wyplacic piniedzy")
#         else:
#             self._balance = wartosc
#
#     @balance.deleter
#     def balance(self):
#         print("Nie mozesz usunac atrybutu balans")
#
#
# konto1 = Konto(12345)
# konto1.numer_konta += 1
# print(konto1.numer_konta)

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        # self to pierwsza współrzędna, other to druga
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def __add__(self,other):
        return Coordinate(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def __len__(self):
        pass

# c = Coordinate(x=3, y=4)
# origin = Coordinate(x=0,y=0)
# print(c.distance(origin))   # Wywołanie metody 'distance' na obiekcie 'c'
# print(c)

# class Valute:
#     def __init__(self,gallions,knut,sickles):
#         self.gallions = gallions
#         self.sickles = sickles
#         self.knut = knut
#     def __add__(self, other):
#         # self to obiekt po lewej stronie (+), other to obiekt po prawej [31, 32]
#         new_gallions = self.gallions + other.gallions
#         new_sickles = self.sickles + other.sickles
#         new_knuts = self.knut + other.knut
#         # Zwracamy nowy obiekt Vault, który jest sumą [33, 34]
#         return Valute(new_gallions,new_knuts,new_sickles)
#     def __str__(self):
#         return f"Gallions:{self.gallions}, Sickles: {self.sickles}, Knuts: {self.knut}"
# if __name__ == "__main__":
#     Potter = Valute(100, 50, 20)
#     Weasly = Valute(25, 50, 20)
#
#     total = Potter + Weasly
#
#     print({f"Potter:{Potter}"})
#     print({f"Weasly:{Weasly}"})
#     print(f"Total:{total}")
class Student:
    def __init__(self, name, house):
        # Wywołanie Settera (dla walidacji)
        self.name = name
        self.house = house

        # Getter dla 'house'
        @property
        def house(self):
            return self._house #zwraca chroniony atrybut

        #tworzmy settera dla Domu
        @house.setter
        def house(self,house):
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                #rzucenie wyjatku w przypadku nieprawidlowaej wartosci
                raise ValueError("Zly Dom")
            self._house= house

        #towrzymy gettera dla name
        @property
        def name(self):
            return self._name

        #towrzymy settera dla name
        @name.setter #nazwa metody + .setter
        def name(self,name):
            if not name:
                raise ValueError("zle Imie kolego :) ")
            self.name = name


