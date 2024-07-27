suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

deck_of_cards = (f"{val} of {suit}" for suit in suits for val in values)

for card in deck_of_cards:
    print(card)
