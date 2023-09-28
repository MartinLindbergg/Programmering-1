
import random
import sys
import os

def clear_terminal():
    os.system("cls")

def avsluta_spel():
    print("Spelet Avslutat")
    sys.exit()

def word_guessing_game():
    while True:
        # Skapa en dictionary med teman och deras motsvarande ordlistor.
        themes = {
            1: ["fläkt", "högtalare", "tangentbord", "mus", "bildskärm", "hörlurar", "musmatta", "lampa", "laddstation"],
            2: ["smör", "mjölk", "ägg", "gurka", "ketchup", "ost", "skinka", "tonfisk", "kikärtor"],
            3: ["läppglans", "mobilladdare", "tuggummi", "hårborste", "deodorant", "strumpor", "reflex", "parfym"]
        }

        # Skriv ut menyn.
        print("╔" + "═" * 22 + "╗")
        print("║____ Ord Gissaren ____║")
        print("║──────────────────────║")
        print("║      Välj Tema       ║")
        print("║                      ║")
        print("║1 Martins Skrivbord   ║")
        print("║2 Martins Kylskåp     ║")
        print("║3 Elenas Handväska    ║")
        print("║──────────────────────║")
        print("║e Avsluta Spel        ║")
        print("╚" + "═" * 22 + "╝")

        # Be spelaren att välja ett menyalternativ.
        selected_theme = input("Välj tema > ")

        # Kontrollera om valt tema är giltigt.
        try:
            selected_theme = int(selected_theme)
            if selected_theme not in themes:
                print("Välj ett giltigt tema (1, 2, eller 3).")
                continue
            
        except ValueError:
            # Om användaren trycker på "e", avsluta spelet.
            if selected_theme == "e":
                avsluta_spel()
            print("Välj ett giltigt tema (1, 2, eller 3).")
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
            guessed_letter = input("Gissa ett ord eller bokstav: ")

            # Kontrollera om spelaren gissade rätt.
            if guessed_letter == word:
                # Spelaren vann!
                clear_terminal()
                print("\U0001f603", "Grattis, du gissade rätt!", "\U0001f603")
                break
            

            # Om spelaren inte gissade rätt, lägg till den gissade bokstaven till listan med gissade bokstäver.
            guessed_letters.append(guessed_letter)

            # Visa spelaren hur många bokstäver de har gissat rätt.
            print("Hint! Du har gissat rätt på följande bokstäver:")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("*", end=" ")
            print()

            # Om spelaren har förbrukat alla sina gissningar, avsluta spelet.
            if len(guessed_letters) == len(word):
                clear_terminal()
                print("\U0001f627", "Du förlorade!","\U0001f627" "\nDet rätta ordet var", word)
                break

        # Fråga användaren om de vill spela igen eller avsluta.
        print("═══════════════════════════════")
        play_again = input("Vill du spela igen? (ja/nej): ")
        if play_again == "ja":
            continue
        elif play_again == "nej":
            avsluta_spel()

if __name__ == "__main__":
    # Anropa spelet.
    word_guessing_game()


