import importlib

def main():
    while True:
        print("Välj ett spel att spela:")
        print("1. Game1")
        print("2. Game2")
        print("3. Game3")
        print("4. Game4")
        print("0. Avsluta")

        choice = input("Ange ditt val: ")

        if choice == "0":
            print("Avslutar programmet.")
            break
        elif choice in ["1", "2", "3", "4"]:
            game_module = importlib.import_module(f"game{choice}")
            game_instance = getattr(game_module, f"Game{choice}")()
            game_instance.play()
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()
