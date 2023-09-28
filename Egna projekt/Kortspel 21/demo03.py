import random

class Card:
    # ... (samma som tidigare)

class Deck:
    # ... (samma som tidigare)

class TwentyOneGame:
    def __init__(self):
        self.user_hand = []
        self.computer_hand = []
        self.deck = Deck()

    # ... (andra metoder är oförändrade)

    def display_cards(self, hand, player_name):
        print(f"{player_name}'s kort:")
        for card in hand:
            card_text = f"{card.rank} av {card.suit}"
            print(card_text.ljust(20), end=" ")  # Justera längden till 20 tecken och skriv bredvid varandra
        print()  # En ny rad för att lägga till en tom rad mellan korten

    def play_game(self):
        print("Välkommen till Tjugoett!")
        self.deal_initial_cards()

        user_wins = self.user_turn()
        if not user_wins:
            self.computer_turn()

        user_value = self.calculate_hand_value(self.user_hand)
        computer_value = self.calculate_hand_value(self.computer_hand)

        self.display_cards(self.user_hand, "Din")
        print(f"Summa: {user_value}")

        self.display_cards(self.computer_hand, "Datorns")
        print(f"Summa: {computer_value}")

        if user_value > 21:
            print("Datorn vinner!")
        elif computer_value > 21 or user_value > computer_value:
            print("Grattis, du vinner!")
        else:
            print("Datorn vinner!")

if __name__ == "__main__":
    game = TwentyOneGame()
    game.play_game()
