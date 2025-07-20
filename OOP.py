class Animal:
    def __init__(self,gatunek,waga,wiek):
        self.gatunek = gatunek
        self.waga = waga
        self.wiek = wiek

    def sleep(self):
        print("zwierze spi")
    def wake_up(self):
        print("zwierze wake up, it's the first day of the month")
dog = Animal("Pies",14,5)
print(dog.waga)