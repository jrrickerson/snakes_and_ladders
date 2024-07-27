import random

BOARD = list(range(1, 101))
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

players = (1, 2)
player_pos = [0, 0]
winner = None

while not winner:
    for player in players:
        # Roll the dice
        roll = random.randint(1, 6)
        print(f"Player {player} rolled a {roll}")

        # Move the player
        new_pos = player_pos[player-1] + roll
        if new_pos in SNAKES_LADDERS:
            if new_pos < SNAKES_LADDERS[new_pos]:
                print(f"Player {player} landed on a Ladder!")
            else:
                print(f"Player {player} landed on a Snake!")
            new_pos = SNAKES_LADDERS[new_pos]
        # Check for a win
        if new_pos == 100:
            print(f"Player {player} wins!")
            winner = player
            break
        # Cannot move past 100
        if new_pos > 100:
            break
        print(f"Player {player} moves to square {new_pos}")
        player_pos[player-1] = new_pos
