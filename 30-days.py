wl = True
while wl:
    try:
        with open("cwel.txt","a")as file:
             plik = input("podaj tresc do pliku:")
             file.write(plik)
    except FileNotFoundError:
        print('nie ma pliku')
    else:
        wl = False

