


"""
BATTLESHIP
grid of 10x10 with 6 ships in different lengths

LEGEND
. = water or empty space
0 = part of the ship
x = part hit with a bullet
# = missed bullet
"""
# global var for grid
grid =[[]]
# var for grid size
grid_size = 10
# var for number of ships
num_of_ships = 6
# var for bullets left
bullets_left = 40
# var for game over
game_over = False
# var for num of ships sunk
num_of_ships_sunk = 0
# var for position of ships
ship_positions = [[]]
# var for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

