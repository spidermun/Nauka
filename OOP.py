import time

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

class bank():
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance




