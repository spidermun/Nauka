import random

words = ("apple", "banana", "orange", "grape", "kiwi", "watermelon")

hangman_art = {
    0: (" ", " ", " "),
    1: (" o", " ", " "),
    2: (" o", "|", " "),
    3: (" o", "/|", " "),
    4: (" o", "/|\\", " "),
    5: (" o", "/|\\", "/ "),
    6: (" o", "/|\\", "/ \\"),
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def main():
    answer = random.choice(words)
    hint = list("_" * len(answer))
    wrong_guesses = 0
    guessed_letters = set()
    wlaczone = True

    while wlaczone:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Zgadnij literę: ").lower()

        if guess in guessed_letters:
            print("Już próbowałeś tej litery.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            print("Nie ma takiej litery!")
            wrong_guesses += 1

        if "_" not in hint:
            display_hint(hint)
            print("Gratulacje! Odgadłeś hasło:", answer)
            wlaczone = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            print("Przegrałeś! Prawidłowe hasło to:", answer)
            wlaczone = False

if __name__ == "__main__":
    main()