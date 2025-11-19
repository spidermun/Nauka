def main():
    print("Cześć! To Twój pierwszy skrypt w Nauka.")
    name = input("Jak masz na imię? ")
    age = input("Ile masz lat? ")
    try:
        age_int = int(age)
        print(f"Hej, {name}! Za rok będziesz mieć {age_int + 1} lat.")
    except ValueError:
        print(f"Hej, {name}! Nie rozpoznałem liczby w polu 'lat'.")

if __name__ == "__main__":
    main()