osoba = {"imie":'Michal',
         "wiek":17,
         "znajomi":["Ola","Kuba"],
         "adres": {
             "miasto":"Krasnystaw",
            "kod_pocztowy":"22-300"
    }
}

print(f"{osoba['imie']} mieszka w {osoba['adres']['miasto']} i ma {osoba['wiek']} lat")