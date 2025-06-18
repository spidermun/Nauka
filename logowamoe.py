import hashlib
users = []
def hashuj_haslo(haslo):
    return hashlib.sha256(haslo.encode()).hexdigest()

def wczytaj_uzytkownikow():
    try:
        with open("users.txt", "r", encoding="utf-8") as f:
            for line in f:
                dane = line.strip().split(";")
                if len(dane) == 4:
                    users.append(dane)
    except FileNotFoundError:
        pass

def zapisz_uzytkownika(imie, nazwisko, haslo, email):
    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{imie};{nazwisko};{haslo};{email}\n")

def main():
    wczytaj_uzytkownikow()
    is_running = True
    while is_running:
        print("== LOGOWANIE ==")
        print("1. Rejestracja")
        print("2. Logowanie")
        print("3. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            haslo = input("Podaj hasło: ")
            email = input("Podaj email: ")
            if imie and nazwisko and haslo and email:
                if any(u[3] == email for u in users):
                    print("Użytkownik z tym adresem email już istnieje!")
                else:
                    haslo = hashuj_haslo(haslo)
                    users.append([imie, nazwisko, haslo, email])
                    zapisz_uzytkownika(imie, nazwisko, haslo, email)
                    print("Rejestracja zakończona pomyślnie!")
            else:
                print("Wszystkie pola są wymagane!")

        if choice == "2":
            login_email = input("Podaj email: ")
            login_haslo = input("Podaj hasło: ")
            login_haslo = hashuj_haslo(login_haslo)
            for user in users:
                if user[3] == login_email and user[2] == login_haslo:
                    print(f"Witaj {user[0]} {user[1]}!")
                    break
            else:
                print("Nieprawidłowy email lub hasło!")

        if choice == "3":
            is_running = False
            print("Do zobaczenia!")

if __name__ == "__main__":
    main()