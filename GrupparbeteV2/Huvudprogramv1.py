from GrupparbeteV2.Wordguessv1 import WordGuessingGame, clear_terminal
from GrupparbeteV2.Stenv1 import RockPaperScissor
import GoFishv1
import GrupparbeteV2.Hangv1 as Hangv1
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
        print("══════════════════════")
        print("(skriv en siffra 1,2,3,4 eller e för att avluta)")
        game_choice = input("Viket spel vill du starta? >")

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
            Hangv1.main()
        elif game_choice == "e":
            clear_terminal()
            print("Programmet Avslutades")
            sys.exit()
        

if __name__ == "__main__":
    main()


