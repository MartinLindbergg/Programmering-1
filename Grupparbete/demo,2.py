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

        # Skapa en lista med bokstäver som spelaren har gissat.
        guessed_letters = []

        # Spela spelet.
        while True:
            # Be spelaren att gissa ett ord.
            guessed_letter = input("Gissa ett ord: ")

            # Kontrollera om spelaren gissade rätt.
            if guessed_letter == word:
                # Spelaren vann!
                print("Grattis, du gissade rätt!")
                break

            # Om spelaren inte gissade rätt, lägg till den gissade bokstaven till listan med gissade bokstäver.
            guessed_letters.append(guessed_letter)

            # Visa spelaren hur många bokstäver de har gissat rätt.
            print("Du har gissat rätt på följande bokstäver:")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("*", end=" ")
            print()

            # Om spelaren har förbrukat alla sina gissningar, avsluta spelet.
            if len(guessed_letters) == len(word):
                print("Du förlorade! Det rätta ordet var", word)
                break

if __name__ == "__main__":
    # Anropa spelet.
    word_guessing_game()
