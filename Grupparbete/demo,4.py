import random

def word_guessing_game():
    """Ett enkelt ordgissningsspel med olika teman."""

    # Skapa en lista med teman.
    themes = ["Martins_skrivbord", "Martins_kylskåp", "Elenas_handväska"]

    # Spela spelet.
    while True:
        # Skriv ut menyn.
        print("*" * 24)
        print("|____ Ord Gissaren ____|")
        print("-" * 24)
        print("|      Välj Tema       |")
        for theme in themes:
            print(f"|{theme}     |")
        print("-" * 24)

        # Be spelaren att välja ett menyalternativ.
        selected_theme = input("Skriv vilket tema du vill spela: ")

        # Kontrollera om temat är giltigt.
        if selected_theme not in themes:
            print("Ogiltigt tema.")
            continue

        # Välj den aktuella listan med ord.
        if selected_theme == "Martins_skrivbord":
            word_list = ["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar", "musmatta",
                        "lampa", "bildskärm", "laddstation", "musmatta"]
        elif selected_theme == "Martins_kylskåp":
            word_list = ["smör", "oliver", "mjölk", "ägg", "proteinbar", "gurka", "ketchup", "äppelmos", "matlåda", "colaburk",
                        "ost", "lingonsylt", "tonfisk", "kikärtor"]
        elif selected_theme == "Elenas_handväska":
            word_list = ["läppglans", "mobilladdare", "våtservätter", "tuggummi", "hårborste", "godis", "deodorant", "strumpor",
                        "reflex", "parfym"]

        # Välj ett ord att gissa.
        word = random.choice(word_list)

        # Skapa en lista med ord som spelaren har gissat.
        guessed_words = []

        # Spela spelet.
        while True:
            # Be spelaren att gissa ett ord.
            guessed_word = input("Gissa ett ord: ")

            # Kontrollera om spelaren gissade rätt ord.
            if guessed_word == word:
                print(f"Grattis, du gissade rätt ord! Ordet var '{word}'.")
                break
            else:
                print("Tyvärr, det är inte rätt ord.")

if __name__ == "__main__":
    # Anropa spelet.
    word_guessing_game()

