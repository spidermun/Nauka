
def main():
    is_running = True
    while is_running:
        print("== LISTA ZAKUPÓW ==")
        print("1.Dodaj produkt")
        print("2.Wyświetl listę")
        print("3.Usuń produkt")
        print("4.Zapisz do pliku")
        print("5.Wczytaj z pliku")
        print("6.Zakończ")
        choice = input("Wybierz opcje:")

        match choice:
            case "1":
                Dodaj_produkt()
            case "2":
                Wyświetl_listę()
            case "3":
                Usuń_produkt()
            case "4":
                Zapisz_do_pliku()
            case "5":
                Wczytaj_z_pliku()
        if choice == "6":
            is_running = False

produkty = []

def Dodaj_produkt():
    print("Dodaj swój produkt('q' aby wyjsc) ")
    while True:
        dodaj = input("Dodaj produkt: ")
        if dodaj.lower() == "q":
            break
        elif dodaj == "":
            print("nie mozesz dodaj pustego produktu!")
        elif dodaj in produkty:
            print("Nie możesz dodać dwa razy tego samego produktu.")
        else:
            produkty.append(dodaj)

def Wyświetl_listę():
    print("wyswietl liste produktów")
    while True:
        print(produkty)
        choice = input("Aby wyjsc wpisz 'q'")
        if choice == "q":
            break

def Usuń_produkt():
    print("Usuń swój produkt('q' aby wyjsc) ")
    print(produkty)
    while True:
        usun = input("Usun produkt: ")
        if usun.lower() == "q":
            break
        if usun in produkty:
            produkty.remove(usun)
            print(f'usunieto {usun}')
        else:
            print("Nie mozesz usunac produktu!")

def Zapisz_do_pliku():
    file_path = 'C:\\Users\\user\\Desktop\\lista.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        for produkt in produkty:
            f.write(produkt + '\n')
    print("Lista została zapisana do pliku na pulpicie.")

def Wczytaj_z_pliku():
    file_path = 'C:\\Users\\user\\Desktop\\lista.txt'
    global produkty
    with open(file_path, 'r', encoding='utf-8') as f:
        produkty = [line.strip() for line in f]
    print("Lista została wczytana z pliku.")
    while True:
        print("Produkty na liście:")
        for produkt in produkty:
            print(f"- {produkt}")
        choice = input("Aby wyjść wpisz 'q': ")
        if choice.lower() == "q":
            break

if __name__ == '__main__':
    main()