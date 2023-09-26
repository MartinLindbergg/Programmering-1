import random

def word_guessing_game():
    # Create a theme list
    themes = ["Martins_skrivbord", "Martins_kylskåp", "Elenas_handväska"]

    while True:
        # Print menu-ui
        print("*" * 24)
        print("|____ Ord Gissaren ____|")
        print("-" * 24)
        print("|      Välj Tema       |")
        for theme in themes:
            print(f"|{theme}     |")
        print("-" * 24)

        # user chooses theme
        selected_theme = input("Skriv vilket tema du vill spela: ")

        # see if theme is viable
        if selected_theme not in themes:
            print("Ogiltigt tema.")
            continue
        print("-" * 50)

        # choose theme based wordlist
        if selected_theme == "Martins_skrivbord":
            word_list = ["fläkt", "högtalare", "tangentbord", "mus", "burk", "snusdosa", "armbandsur", "hörlurar", "musmatta",
                        "lampa", "bildskärm", "laddstation", "musmatta"]
        elif selected_theme == "Martins_kylskåp":
            word_list = ["smör", "oliver", "mjölk", "ägg", "proteinbar", "gurka", "ketchup", "äppelmos", "matlåda", "colaburk",
                        "ost", "lingonsylt", "tonfisk", "kikärtor"]
        elif selected_theme == "Elenas_handväska":
            word_list = ["läppglans", "mobilladdare", "våtservätter", "tuggummi", "hårborste", "godis", "deodorant", "strumpor",
                        "reflex", "parfym"]

        # Choose a word from the themelist
        word = random.choice(word_list)

        # Create an empty list that saves input letters
        guessed_letters = []

        # Create an empty list that saves the correct letters from input
        correct_guesses = []

        while True:
            # User letter input
            guessed_letter = input("Skriv en bokstav som du tror finns i ordet: ")
            print("-" * 50)

            # Check if the user guessed correct letter
            if guessed_letter in word:
                print(f"Rätt! '{guessed_letter}' finns i ordet.")
                correct_guesses.append(guessed_letter)
            else:
                print(f"Tyvärr, '{guessed_letter}' finns inte i ordet.")

            # Show user the amount of correct guessed letters
            display_word = ""
            for letter in word:
                if letter in correct_guesses:
                    display_word += letter
                else:
                    display_word += "*"

            print(f"Rätt ord: {display_word}")

            # If user correctly guessed the whole word, end game
            if display_word == word:
                    print("********    *********     *")
                    print("**               ***      *")
                    print("**  ****        ***       *")
                    print("**     **      **          ")
                    print("*********    *********    *")
                    print("Grattis, du gissade rätt ord!")
                    print("---------------------------")
                    break

if __name__ == "__main__":
    # call game
    word_guessing_game()



'''
Att fixa:
Ui-layout
kortkommando för att välja tema
exit-knapp
programmet ska fråga användare "spela igen?" istället för att direkt starta om
printa ut Grattis meddelande snyggare
'''






'''
Tänka om och starta från början?
Vill egentligen att användare ska gissa ord istället för bokstäver
Om en korrekt bokstav finns med i ordet som användaren gissat, spara och printa ut som ledtråd.

'''

