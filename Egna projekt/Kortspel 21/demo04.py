def deal_initial_cards(self):
    user_card1 = self.deck.draw_card()
    user_card2 = self.deck.draw_card()
    computer_card1 = self.deck.draw_card()
    computer_card2 = self.deck.draw_card()

    self.user_hand.extend([user_card1, user_card2])
    self.computer_hand.extend([computer_card1, computer_card2])

    print("Dina kort:")
    print(f"{user_card1.rank} av {user_card1.suit}".ljust(20), end=" ")
    print(f"{user_card2.rank} av {user_card2.suit}")
    print("\nDatorns kort:")
    print(f"{computer_card1.rank} av {computer_card1.suit}".ljust(20), end=" ")
    print(f"{computer_card2.rank} av {computer_card2.suit}")

deal_initial_cards()

'''
            for card in self.user_hand:
                print("╔════════╗")
                print(f"║{card.suit} {card.rank}     ║")
                print("║        ║")
                print("║        ║")
                print(f"║     {card.rank} {card.suit}║")
                print("╚════════╝")
'''