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

    elif direction == "down":
            if row + length >= grid_size:
                                return False
                                end_row  = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

""" create grid and place ships randomly """
def create_grid():

    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
            grid.append(row)

            num_of_ships_placed = 0

            ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_cols = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

      
    def print_grid():
       """Will print the grid with rows A-J and columns 0-9"""
       global grid
       global alphabet

    debug_mode = True
    
    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "0":
                if debug_mode:
                    print("0", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

"""get valid row and col to place bullet"""
def accept_bullet():

    global alphabet
    global grid

    is_valid_bullet = False
    row = -1
    col = -1
    while is_valid_bullet is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row - alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("Already hit!, Shoot somewhere else :)")
            continue
        if grid[col][row] == "." or grid[col][row] == "0":
            is_valid_bullet = True
            
            return row, col

    def check_ship_sunk(row, col):
        """When all parts of the ships are hit and the ship sinks"""
        global ship_positions
        global grid

        for position in ship_positions:
            start_row = position[0]
            end_row = position[1]
            start_col = position[2]
            end_col = position[3]
            if start_row <= row <= end_row and start_col <= col <= end_col:
                # Check if the whole ship is sunk
                for r in range(start_row, end_row):
                    for c in range(start_col, end_col):
                        if grid[r][c] != "X":
                            return False
        return True

    def fire_bullet():
        """After bullet being shut this will adjust the grid accordingly"""
        global grid
        global num_of_ships_sunk
        global bullets_left

        row, col = accept_bullet()
        print("")
        print("----------------------------")

        if grid[row][col] == ".":
            print("Missed it! Better luck next time!")
            grid[row][col] = "#"
        elif grid[row][col] == "0":
            print("Nice shot!", end=" ")
            grid[row][col] = "X"
            if check_ship_sunk(row, col):
                print("A ship is down! Yeah!")
                num_of_ships_sunk += 1
            else:
                print("Yeah! You shot a ship!")

        bullets_left -= 1

    def check_game():
      """"In case there all bullets are used or all ships are down"""
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("YEAH, you won!!")
        game_over = True
    elif bullets_left <= 0:
        print("No more bullets! Better luck next time!")
        game_over = True

    def main():
        """"Entry point of the app that runs the game loop"""
        global game_over

        print("-----Are you ready for Battleships?-----")
        print("Let's battle! U have 40 bullets and 6 ships to hit!")

        create_grid()

        while game_over is False:
            print_grid()
            print("Remaining ships: " + str(num_of_ships - num_of_ships_sunk))
            print("Remaining bullets: " + str(bullets_left))
            fire_bullet()
            print("----------------------------")
            print("")
            check_game()

    if __name__ == '__main__':
       """Will only be called when program is run from terminal or an IDE like PyCharms"""
       main()        
