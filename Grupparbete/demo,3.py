import random

def word_guessing_game():
    """Ett enkelt ordgissningsspel med olika teman."""

    # Skapa en lista med teman
    themes = ["Martins_skrivbord", "Martins_kylskåp", "Elenas_handväska"]

    while True:
        # Skriv ut meny-ui
        print("*" * 24)
        print("|____ Ord Gissaren ____|")
        print("-" * 24)
        print("|      Välj Tema       |")
        for theme in themes:
            print(f"|{theme}     |")
        print("-" * 24)

        # Användare väljer tema
        selected_theme = input("Skriv vilket tema du vill spela: ")

        # Kontrollera om temat finns
        if selected_theme not in themes:
            print("Ogiltigt tema.")
            continue
        print("-" * 50)

        # Väljer lista med ord baserat på tema
        if selected_theme == "Martins_skrivbord":
            word_list = ["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar", "musmatta",
                        "lampa", "bildskärm", "laddstation", "musmatta"]
        elif selected_theme == "Martins_kylskåp":
            word_list = ["smör", "oliver", "mjölk", "ägg", "proteinbar", "gurka", "ketchup", "äppelmos", "matlåda", "colaburk",
                        "ost", "lingonsylt", "tonfisk", "kikärtor"]
        elif selected_theme == "Elenas_handväska":
            word_list = ["läppglans", "mobilladdare", "våtservätter", "tuggummi", "hårborste", "godis", "deodorant", "strumpor",
                        "reflex", "parfym"]

        # Väljer ord från temat
        word = random.choice(word_list)

        # Skapa en lista med bokstäver som spelaren har gissat
        guessed_letters = []

        # Skapa en lista med rätt gissade bokstäver
        correct_guesses = []

        while True:
            # Användaren gissar en bokstav
            guessed_letter = input("Skriv en bokstav som du tror finns i ordet: ")
            print("-" * 50)

            # Kontrollera om spelaren gissade rätt bokstav
            if guessed_letter in word:
                print(f"Rätt! '{guessed_letter}' finns i ordet.")
                correct_guesses.append(guessed_letter)
            else:
                print(f"Tyvärr, '{guessed_letter}' finns inte i ordet.")

            # Visa spelaren hur många rätt gissade bokstäver
            display_word = ""
            for letter in word:
                if letter in correct_guesses:
                    display_word += letter
                else:
                    display_word += "*"

            print(f"Rätt ord: {display_word}")

            # Om spelaren har gissat hela ordet, avsluta spelet
            if display_word == word:
                print("Grattis, du gissade rätt ord!")
                break

if __name__ == "__main__":
    # Anropa spelet
    word_guessing_game()
