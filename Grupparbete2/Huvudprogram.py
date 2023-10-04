from Wordguess import WordGuessingGame, clear_terminal
from Sten import RockPaperScissor
import GoFish
import Hang
import sys

def main():
    while True:
        # Skriv ut menyn.
        clear_terminal()
        print("Välj ett spel:")
        print("1 Ordgissaren")
        print("2 Sten, Sax, Påse")
        print("3 Finns i Sjön")
        print("4 Hängagubbe")
        print("e Avlsuta Programmet")

        # Läs in användarens val.
        game_choice = input("Välj ett spel > ")

        # Starta spelet om användaren väljer "Ordgissaren".
        if game_choice == "1":
            clear_terminal()
            WordGuessingGame()
        elif game_choice == "2":
            game = RockPaperScissor()
            game.play()
        elif game_choice == "3":
            GoFish.main_game()
        elif game_choice == "4":
            clear_terminal()
            Hang.main()
        elif game_choice == "e":
            clear_terminal()
            print("Programmet Avslutades")
            sys.exit()


if __name__ == "__main__":
    main()


