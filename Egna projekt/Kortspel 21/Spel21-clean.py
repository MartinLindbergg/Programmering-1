
import random
import sys

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in "J":
            return 11
        elif self.rank in "Q":
            return 12
        elif self.rank in "K":
            return 13
        elif self.rank == "A":
            return 1  
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J", "A"]
        suits = ["♥", "♦", "♣", "♠"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

class TwentyOneGame:
    def __init__(self):
        self.user_hand = []
        self.computer_hand = []
        self.deck = Deck()

    def deal_initial_cards(self):
        self.user_hand.append(self.deck.draw_card())
        self.computer_hand.append(self.deck.draw_card())
        self.computer_hand.append(self.deck.draw_card())

    def calculate_hand_value(self, hand):
        value = sum(card.value() for card in hand)
        if value <= 7 and any(card.rank == "Ess" for card in hand):
            value += 14
        return value

    def user_turn(self):
        while True:
            print("Dina kort:")
            cards = []
            for card in self.user_hand:
                print("╔════════╗")
                print(f"║{card.suit} {card.rank}     ║")
                print("║        ║")
                print("║        ║")
                print(f"║     {card.rank} {card.suit}║")
                print("╚════════╝")
 
                
            user_value = self.calculate_hand_value(self.user_hand)
            print(f"Summa: {user_value}")

            if user_value == 21:
                print("Grattis, du har fått 21! Du vinner!")
                return True
            elif user_value > 21:
                print("Du har överstigit 21. Du förlorar.")
                return False

            choice = input("Vill du dra ett till kort? (ja/nej): ").lower()
            if choice == "ja":
                self.user_hand.append(self.deck.draw_card())
            else:
                return False

    def computer_turn(self):
        while True:
            computer_value = self.calculate_hand_value(self.computer_hand)

            if computer_value >= 17:
                return False

            self.computer_hand.append(self.deck.draw_card())

    def play_game(self):
        print("Välkommen till Tjugoett!")
        self.deal_initial_cards()

        user_wins = self.user_turn()
        if not user_wins:
            self.computer_turn()

        user_value = self.calculate_hand_value(self.user_hand)
        computer_value = self.calculate_hand_value(self.computer_hand)

        print("\nDin hand:")
        for card in self.user_hand:
            print(f"{card.suit} {card.rank}")
        
        print(f"Summa: {user_value}")

        print("\nDatorns hand:")
        for card in self.computer_hand:
            print(f"{card.suit} {card.rank}")
        print(f"Summa: {computer_value}")

        if user_value > 21:
            print("Datorn vinner!")
        elif computer_value > 21 or user_value > computer_value:
            print("Grattis, du vinner!")
        else:
            print("Datorn vinner!")
        
        play_again = input("Vill du spela igen?: ")
        if play_again == "ja":
            new_game = TwentyOneGame()
            new_game.play_game()
        elif play_again == "nej":
            print("Spelet Avslutat")
            sys.exit()

if __name__ == "__main__":
    game = TwentyOneGame()
    game.play_game()

