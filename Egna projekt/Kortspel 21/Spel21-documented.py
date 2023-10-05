# importera random-modul för att slumpmässigt dra kort
import random
# Importera sys-modul för att avsluta spelet baserat på input värde
import sys
# Importera os-modul för att rensa terminalen
import os

# Funktion för att rensa terminalen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Klassen "Card" representerar ett spelkort
class Card:
    def __init__(self, rank, suit):
        self.rank = rank  # Värdet på kortet (2, 3, ..., K, Q, J, A)
        self.suit = suit  # Färgen på kortet (♥, ♦, ♣, ♠)

    # Funktion för att räkna ut värdet på korten.
    def value(self):
        if self.rank in "J":        # Knekt är värt 11
            return 11
        elif self.rank in "Q":      # Dam är värt 12
            return 12
        elif self.rank in "K":      # Kung är värt 13
            return 13
        elif self.rank == "A":      # Ess är till en början värt 1 (men kan ändras beroende på vilka kort spelaren har)
            return 1
        else:
            return int(self.rank)   # Resten av kortet är värt samma som värdet på kortet (2 är värt 2, 3 är värt 3 osv)

# Klassen "Deck" representerar kortleken
class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J", "A"]
        suits = ["♥", "♦", "♣", "♠"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)  # Korten generaras slumpmässigt

    # Funktion för att dra ett kort från kortleken
    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

# Klassen TwentyOneGame representerar själva spelet "21"
class TwentyOneGame:
    def __init__(self):
        self.user_hand = []        # Spelarens hand
        self.computer_hand = []    # Datorns hand
        self.deck = Deck()         # Kortleken

    # Funktion för att dela ut det första kortet till spelaren (Sedan drar datorn 2 kort samtidigt )
    def deal_initial_cards(self):
        self.user_hand.append(self.deck.draw_card())
        self.computer_hand.append(self.deck.draw_card())
        self.computer_hand.append(self.deck.draw_card())

    # Funktion för att räkna ut värdet av en hand
    def calculate_hand_value(self, hand):
        value = sum(card.value() for card in hand)
        if value <= 7 and any(card.rank == "A" for card in hand): 
            value += 14  # Om värdet på handen är mindre eller lika med 7 så blir värdet på Ess 14 istället för 1.
        return value

    # Funktion där spelaren drar sina kort
    def user_turn(self):
        while True:
            print("Dina kort:")
            cards = []  # Denna lista skapas när spelaren drar sitt första kort, och sparar korten som spelaren har på handen
            for card in self.user_hand:
                print("╔════════╗")
                print(f"║{card.suit} {card.rank}     ║")
                print("║        ║")                         # Ui på korten som spelaren drar
                print("║        ║")
                print(f"║     {card.rank} {card.suit}║")
                print("╚════════╝")

            user_value = self.calculate_hand_value(self.user_hand)
            print(f"Summa: {user_value}")   # Skriver ut summan av värdet på spelarens hand

            if user_value == 21:
                print("Grattis, du har fått 21! Du vinner!") # Om spelaren får summan 21 vinner spelaren.
                return True
            elif user_value > 21:
                print("Du har överstigit 21. Du förlorar.") # Om spelaren överstiger 21 förlorar spelaren
                return False

            choice = input("Vill du dra ett till kort? (ja/nej): ").lower() # Input frågar om spelare vill dra ett till kort
            if choice == "ja":
                self.user_hand.append(self.deck.draw_card()) # Korten som dras försvinner från kortleken
            else:
                return False

    # Funktion där datorn drar sina kort
    def computer_turn(self):
        while True:
            computer_value = self.calculate_hand_value(self.computer_hand)

            if computer_value >= 17:    # Om datorns hand har summan 17 eller mer så drar inte datorn några fler kort
                return False

            self.computer_hand.append(self.deck.draw_card()) # Korens som dras försvinner från kortleken

    # Funktion för att spela spelet
    def play_game(self):
        print("Välkommen till Tjugoett!")
        self.deal_initial_cards() # Delar ut korten

        user_wins = self.user_turn()
        if not user_wins:
            self.computer_turn()

        user_value = self.calculate_hand_value(self.user_hand) # Summan av spelarens hand
        computer_value = self.calculate_hand_value(self.computer_hand) # Summan av datorns hand

        print("\nDin hand:")
        for card in self.user_hand:
            print(f"{card.suit} {card.rank}") # Skriver ut spelarens hand
        print(f"Summa: {user_value}") # Skriver ut summan av spelarens hand

        print("\nDatorns hand:")
        for card in self.computer_hand:
            print(f"{card.suit} {card.rank}") # Skriver ut datorns hand
        print(f"Summa: {computer_value}") # Skriver ut summan av datorns hand

        if user_value > 21:
            print("Datorn vinner!") # Om spelarens summa överstiger 21 vinner datorn
        elif computer_value > 21 or user_value > computer_value:
            print("Grattis, du vinner!") # Spelaren vinner om datorns summa överstiger 21 eller om datorns summa är mindre än spelarens summa
        else:
            print("Datorn vinner!")
        print("══════════════════════")

        play_again = input("Vill du spela igen?: ") # Frågar om användaren vill spela igen
        if play_again == "ja":
            clear_terminal() # Rensar terminalen
            new_game = TwentyOneGame()
            new_game.play_game() # Om input == ja så startas ett nytt spel
        elif play_again == "nej":
            clear_terminal()
            print("Spelet Avslutat")
            sys.exit() # Om input == nej så avslutas programet

# Kör spelet om filen körs som ett fristående program
if __name__ == "__main__":
    game = TwentyOneGame()
    game.play_game()


# Kort summering av spelet

'''

I detta spel gäller det att komma så nära 21 som möjligt. Spelaren drar ett kort i taget och får frågan om att dra ett till
kort. Om spelaren drar korten av summan 21 så vinner spelaren. Drar spelaren korten av summan över 21 så förlorar spelaren.
Spelaren kan även vinna genom att stanna närmare 21 än datorn.

'''