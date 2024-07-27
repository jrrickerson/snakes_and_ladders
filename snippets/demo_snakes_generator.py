import random

SNAKES_LADDERS = {
    1: 38,
    4: 14,
    9: 31,
    16: 6,
    21: 42,
    28: 84,
    36: 44,
    47: 26,
    49: 11,
    51: 67,
    56: 53,
    62: 19,
    64: 60,
    71: 91,
    80: 100,
    87: 24,
    93: 73,
    95: 75,
    98: 78,
}


def gen_players():
    while True:
        yield 1
        yield 2


def gen_dice():
    while True:
        yield random.randint(1, 6)


def gen_position(roll):
    pos = 0
    while True:
        new_pos = pos + roll
        if new_pos in SNAKES_LADDERS:
            snake_ladder_pos = SNAKES_LADDERS[new_pos]
            if snake_ladder_pos > new_pos:
                print("Landed on a ladder!")
            else:
                print("Landed on a snake!")
            new_pos = snake_ladder_pos
        if new_pos <= 100:
            pos = new_pos
        roll = yield new_pos


# Create a dice generator
dice = gen_dice()
# Create two board generators
boards = (gen_position(0), gen_position(0))
winner = None

# Initialize the boards at position 0
next(boards[0])
next(boards[1])

while not winner:
    for player in gen_players():
        roll = next(dice)
        print(f"Player {player} rolled a {roll}")
        board = boards[player-1]
        space = board.send(roll)
        print(f"Player {player} moved to {space}")
        if space == 100:
            winner = player
            print(f"Player {player} wins!")
            break
