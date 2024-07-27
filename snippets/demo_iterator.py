"""Build our own Iterator class that iterates over names of chess pieces"""
class ChessPieces:
    names = [
        "pawn",
        "rook",
        "knight",
        "bishop",
        "queen",
        "king",
    ]
    def __init__(self):
        self.position = 0

    def __iter__(self):
        print("Called __iter__!")
        self.position = 0
        return self

    def __next__(self):
        print("Called __next__!")
        if self.position == len(self.names):
            raise StopIteration("No more names!")
        item = self.names[self.position]
        self.position += 1
        return item

        
