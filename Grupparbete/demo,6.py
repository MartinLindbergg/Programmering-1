import random

def word_guessing_game():
    """Ett enkelt ordgissningsspel med olika teman."""

    # Skapa en dictionary med teman och deras motsvarande ordlistor.
    themes = {
        1: ["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar", "musmatta",
            "lampa", "bildskärm", "laddstation", "musmatta"],
        2: ["smör", "oliver", "mjölk", "ägg", "proteinbar", "gurka", "ketchup", "äppelmos", "matlåda", "colaburk",
            "ost", "lingonsylt", "tonfisk", "kikärtor"],
        3: ["läppglans", "mobilladdare", "våtservätter", "tuggummi", "hårborste", "godis", "deodorant", "strumpor",
            "reflex", "parfym"]
    }

    while True:
        # Skriv ut menyn.
        print("*" * 24)
        print("|____ Ord Gissaren ____|")
        print("|", "-" * 20, "|")
        print("|      Välj Tema       |")
        print("|1 Martins Skrivbord   |")
        print("|2 Martins Kylskåp     |")
        print("|3 Elenas Handväska    |")
        print("*" * 24)

        # Be spelaren att välja ett menyalternativ.
        selected_theme = input("Skriv en siffra för att välja tema: ")

        # Kontrollera om valt tema är giltigt.
        try:
            selected_theme = int(selected_theme)
            if selected_theme not in themes:
                print("Ogiltigt tema.")
                continue
        except ValueError:
            print("Ogiltigt! (skriv 1,2 eller 3)")
            continue

        # Välj den aktuella listan med ord från dictionaryn.
        word_list = themes[selected_theme]

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
