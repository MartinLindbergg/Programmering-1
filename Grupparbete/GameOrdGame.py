from GameOrdGame import WordGuessingGame

# Skapa en klass för varje spel
class GameGo:
    def play(self):
        print("Spela spel 1")

class GameHang:
    def play(self):
        print("Spela spel 3")

class GameSten:
    def play(self):
        print("Spela spel 4")

# Skapa en klass för spelmenyn
class GameMenu:
    def __init__(self):
        self.games = [GameGo(), WordGuessingGame(), GameHang(), GameSten()]


    def display_menu(self):
        print("Välkommen till spelmenyn:")
        for i, game in enumerate(self.games):
            print(f"{i + 1}. Spel {i + 1}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Välj ett spel (1-4) eller 'q' för att avsluta: ")
            
            if choice == 'q':
                print("Hej då!")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 4:
                game_index = int(choice) - 1
                selected_game = self.games[game_index]

                # Om spelaren väljer spel 2, starta spelet.
                if game_index == 1:
                    selected_game.play()
                else:
                    selected_game.play()
            else:
                print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    # Skapa ett objekt av den uppdaterade klassen
    game = WordGuessingGame()
    menu = GameMenu()
    menu.run()
