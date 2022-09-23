from random import randint

board = []
""" The board will represent the ocean for the battleship """

for x in range(5):
    board.append(["O"] * 5)
""" create board of 5 by 5 """


def print_board(board):
    for row in board:
        print" ".join(row)


print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)
"""to acces random rows"""


def random_col(board):
    return randint(0, len(board), - 1)
"""to acces random cols"""
ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Which row?: "))
    guess_col = int(raw_input("Which col?: "))
    if guess_row == ship_row and guess_col == ship_col:
        print "Wow, you hit the right spot!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or
(guess_col < 0 or guess_col > 4):
        print "Haha, wrong spot!"
        elif(board[guess_row][guess_col] == "X"):
            print "You've already hit this one!"
        else:
            print "Too bad! You didn't hit the battleship"
            board[guess_row][guess_col] = "X"
            print_board(board)
        if (turn == 3):
            print "Better luck next time! This game is over"