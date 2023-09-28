def word_guessing_game():
    """Ett enkelt ordgissningsspel med olika teman."""

    # Skapa en lista med teman och deras motsvarande siffror.
    themes = []
    for theme in ["Martins_skrivbord", "Martins_kylskåp", "Elenas_handväska"]:
        themes.append((theme, 1 + themes.index(theme)))

    # Spela spelet.
    while True:
        # Skriv ut menyn.
        print("*" * 24)
        print("|____ Ord Gissaren ____|")
        print("-" * 24)
        print("|      Välj Tema       |")
        for theme, theme_number in themes:
            print(f"|{theme_number}. {theme}     |")
        print("-" * 24)

        # Be spelaren att välja ett menyalternativ.
        theme_choice = input("Välj ett nummer: ")

        # Kontrollera om temat finns i listan.
        if theme_choice not in themes:
            print("Ogiltigt tema.")
            continue

        # Välj den aktuella listan med ord.
        theme = themes[theme_choice][0]
        if theme == 1:
            word_list = ["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar", "musmatta",
                        "lampa", "bildskärm", "laddstation", "musmatta"]
        elif theme == 2:
            word_list = ["smör", "oliver", "mjölk", "ägg", "proteinbar", "gurka", "ketchup", "äppelmos", "matlåda", "colaburk",
                        "ost", "lingonsylt", "tonfisk", "kikärtor"]
        elif theme == 3:
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
                print(f"Grattis, du gissade rätt! Ordet var '{word}'.")
                break
            else:
                print("Tyvärr, det är inte rätt ord.")

if __name__ == "__main__":
    # Anropa spelet.
    word_guessing_game()
