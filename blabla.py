# Opis zadania:
# Zbudujemy program do zarządzania zadaniami (to-do listę), który będzie działał w terminalu. Funkcjonalności:
#
# Dodaj zadanie – podajesz tekst zadania, które trafia na listę.
#
# Pokaż zadania – wyświetlasz listę wszystkich zadań, z oznaczeniem czy wykonane.
#
# Oznacz zadanie jako wykonane – wybierasz zadanie i oznaczasz je jako zrobione.
#
# Usuń zadanie – możesz usunąć zadanie z listy.
#
# Wyjście – kończysz działanie programu.


tasks = []
def main():
    is_run = True
    while is_run:
        print("Wybierz opcję:")
        print("1. Dodaj zadanie")
        print("2. Pokaż zadania")
        print("3. Oznacz zadanie jako wykonane")
        print("4. Usuń zadanie")
        print("5. Wyjście")

        choice = input("Wybierz opcje (1-5):")
        if choice == "1":
            Dodaj_zadanie()
        elif choice == "2":
            Pokaż_zadania()

        elif choice == "3":
            Oznacz_zadanie_jako_wykonane()
        elif choice == "4":
            Usuń_zadanie()
        elif choice == "5":
            is_run = False
            print("Bywaj!")
        else:
            print("Musisz podac opcje od 1 do 5!")

def Dodaj_zadanie():
    print("Dodaj zadanie")
    task = input("Wpisz tresc ktory chcesz dodac:")
    if task == "":
        print("________________________")
        print("Nie mozesz dodac pustego zadania!")
        print("________________________")
    else:
        tasks.append(task)
        print("________________________")
        print("Zadanie dodane do listy!")
        print("________________________")


def Pokaż_zadania():
    print("________________________")
    for i in range(len(tasks)):

        print(f"{i + 1}. {tasks[i]}")
    print("________________________")
def Oznacz_zadanie_jako_wykonane():
    print("Oznacz zadanie jako wykonane")
    Pokaż_zadania()
    task_num = int(input("Wypisz numer zadania,ktore chcesz zaznaczyc jako wykonane:"))
    if task_num <= 0 or task_num > len(tasks):
        print("________________________")
        print("Nie ma takiego zadania!")
        print("________________________")
    else:
        tasks[task_num - 1] += " (wykonane)"
        print("________________________")
        print("Zadanie oznaczone jako wykonane!")
        print("________________________")
def Usuń_zadanie():
    print("Usuń zadanie")
    Pokaż_zadania()
    task_num = int(input("Wypisz numer zadania do usuniecia: "))
    if task_num <= 0 or task_num > len(tasks):
        print("________________________")
        print("Nie ma takiego zadania!")
        print("________________________")
    else:
        del tasks[task_num - 1]
        print("________________________")
        print("Zadanie usunięte!")
        print("________________________")

if __name__ == "__main__":
    main()
