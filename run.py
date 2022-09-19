import random
import time


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

"""check row or column to place ship"""
def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            grid[r][c] != ".":
            all_valid= False
            break
        if all_valid: 
            ship_positions.append([start_row, end_row, start_col, end_col])
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    grid[r][c] = "0"
                    return all_valid

"""place ship on grid"""
def try_to_place_ship_on_grid(row, col, direction, length):
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
            start_col = col - length + 1

    elif direction == "right":
            if col + length >= grid_size:
                return False
                end_col = col + length

     elif direction == "up":
        if row - length < 0:
                        return False
                        start_row = row - length + 1

     elif direction = "left":
        if row + length >= grid_size:
                                return False
                                end_row  = row + length

return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


