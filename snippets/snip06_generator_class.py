
class Deck:
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    def __iter__(self):
        for suit in self.suits:
            for val in self.values:
                yield f"{val} of {suit}"

    # No need for __next__()
