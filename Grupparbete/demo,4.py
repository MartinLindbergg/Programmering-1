import random

# Antal korrekt gissade bokstäver
correct_guesses = 0

def display_correct_guesses(word, correct_guesses):
    """Visar användaren antalet korrekt gissade bokstäver."""

    display_word = ""
    for letter in word:
        if letter in correct_guesses:
            display_word += letter
        else:
            display_word += "*"

    print(display_word)

def word_guessing_game():
    """Ett enkelt ordgissningsspel med olika teman."""

    # Skapa en lista med teman.
    themes = [1, 2, 3]

    # Skapa en variabel för temat.
    current_theme = None

    # Spela spelet.
    while True:
        # Skriv ut menyn.
        print("*" * 24)
        print("|____ Ord Gissaren ____|")
        print("|","-" * 20, "|")
        print("|      Välj Tema       |")
        print("|1 Martins Skrivbord   |")
        print("|2 Martins Kylskåp     |")
        print("|3 Elenas Handväska    |")
        print("*" * 24)

        # Be spelaren att välja ett tema.
        selected_theme = input("Skriv en siffra för att välja tema: ")

        # Kontrollera om temat är giltigt.
        if selected_theme not in themes:
            print("Ogiltigt tema.")
            continue

        # Konvertera spelarens inmatning till ett heltal.
        selected_theme_int = int(selected_theme)

        # Sätt värdet på den nya variabeln.
        current_theme = selected_theme_int

        # Kontrollera om det konverterade heltalvärdet är ett giltigt tema.
        if selected_theme_int not in themes:
            current_theme = None

        # Välj den aktuella listan med ord.
        if current_theme == 1:
            word_list = ["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar", "musmatta",
                        "lampa", "bildskärm", "laddstation", "musmatta"]
        elif current_theme == 2:
            word_list = ["smör", "oliver", "mjölk", "ägg", "proteinbar", "gurka", "ketchup", "äppelmos", "matlåda", "colaburk",
                        "ost", "lingonsylt", "tonfisk", "kikärtor"]
        elif current_theme == 3:
            word_list = ["läppglans", "mobilladdare", "våtservätter", "tuggummi", "hårborste", "godis", "deodorant", "strumpor",
                        "reflex", "parfym"]

        # Välj ett ord att gissa.
        word = random.choice(word_list)

        # Skapa en lista med bokstäver som spelaren har gissat.
        guessed_letters = []

        # Spela spelet.
        while True:
            # Be spelaren att gissa en bokstav.
            guessed_letter = input("Gissa en bokstav: ")

            # Kontrollera om bokstaven finns i ordet.
            if guessed_letter in word:
                correct_guesses += 1
                guessed_letters.append(guessed_letter)

            # Visa antalet korrekt gissade bokstäver.
            display_correct_guesses(word, correct_guesses)

            # Kontrollera om spelaren har gissat rätt ord.
            if guessed_letters == word:
                print(f"Grattis, du gissade rätt")
            
            if __name__ == "__main__":
             # Anropa spelet.
               word_guessing_game()
