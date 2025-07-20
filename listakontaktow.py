# Opis:
# Stwórz program, który pozwala użytkownikowi:
#
# Dodać kontakt (imię i numer telefonu)
# Usunąć kontakt według imienia
# Wyświetlić wszystkie kontakty
# Sprawdzić, czy kontakt istnieje

slownik = {}

def dodaj_imie():
    print("Dodaj Kontakt!")
    klucz = input("Podaj Imie: ")
    wartosc = input("Podaj Numer tel: ")
    slownik[klucz] = wartosc
    print("dodane!")
def usun_imie():
    print("Usun kontakt!")
    klucz = input("Podaj imie do usuniecia!: ")
    if klucz in slownik.keys():
        del slownik[klucz]
        print("Usunieto kontakt!")
def wyswietl_wszytko():
    print("Wyswietl wszytko!")
    for klucz,wartosc in slownik.items():
        print(f"Imie: {klucz}, Numer tel: {wartosc}")
def sprawdz():
    print("Sprawdzić, czy kontakt istnieje!")
    klucz = input("Podaj imię kontaktu!: ").lower()
    if klucz in slownik:
        print(f"Kontakt istnieje! Imię: {klucz}, Numer tel: {slownik[klucz]}")
    else:
        print("Kontakt nie istnieje!")
def main():
    wlacznik = True
    while wlacznik:
        print('______________')
        print("1. Dodać kontakt ")
        print("2. Usunąć kontakt ")
        print("3. wyswietl wszytkie kontakty ")
        print("4. sprawdz czy kontakt istnieje")
        print(" q aby wyjsc z programu")
        print('______________')
        choice = input("Podaj od 1-4: ")
        match choice:
            case "1":
                dodaj_imie()
            case "2":
                usun_imie()
            case "3":
                wyswietl_wszytko()
            case "4":
                sprawdz()
            case "q":
                wlacznik = False
            case _:
                print("nie znaleziono...")

if __name__ == "__main__":
    main()