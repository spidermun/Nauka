wlacznik = True
while True:
    try:
        do_pliku = str(input("Wpisz Zadanie na dzis:"))
    except TypeError:
        print("Tylko litery!")
    except ValueError:
        print("Tylko litery!")
    else:
        if do_pliku == "q":
            break
        else:
            with open("text.tx","a")as file:
                file.write(do_pliku + "\n")
                print("dodałem do pliku")
