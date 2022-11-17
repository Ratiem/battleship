"""
A simple Battleship game of a single user playing against computer board.
"""
# Display greetings message to the user
# Request user name
# The player grid displays for the user to commence the game
#   Create Grid
#       Row headers
#       Column headers
#       Grid body
#   Display Grid
# Get user input
# Start turns
# As the user, guess the location of the ship
# Check if duplicate guess
# Check for hit or miss
# Check for win or lose
# At end of game run new game

LETTER_TO_NUM = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
    }

def display_greetings_message():
    """
    Display greetings message to the user
    """
    print("-" * 50)
    print("Welcome to the battleships game!!")
    print("-" * 50)


class ShipBoard:
    """
    Main Board class
    """

    def __init__(self, board, name):
        self.board = board
        self.name = name

    def print_board(self):
        """
        Print the board
        """
        print(self.name)
        print("  A B C D E F G H")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


def guess():
    try:
        x_row = int(input("Enter the row number of the ship: "))
        while 1 > x_row or x_row > 8:
            print("Not a valid choice, please enter a valid row number")
            x_row = int(input("Enter the row number of the ship: "))
    except (ValueError, KeyError):
        print("Not a valid choice, please enter a valid row number")
        return guess()
    try:
        y_column = input("Enter the column letter of the ship ").upper()
        while y_column not in 'ABCDEFGH':
            print("Not a valid choice, please enter a valid column letter")
            y_column = input("Enter the column letter of the ship ").upper()
        return int(x_row) - 1, LETTER_TO_NUM[y_column]
    except (ValueError, KeyError):
        print("Not a valid choice, please enter a valid column letter")
        return guess()


def new_game():
    """
    Create a new game
    """
    display_greetings_message()
    name = input("Please enter your name: \n")
    while not name:
        print("This is not a valid name")
        name = input("Please enter your name: \n")  
    user_board = ShipBoard(
        [[" "] * 8 for i in range(8)],
        f"{name}'s Board")
    computer_board = ShipBoard(
        [[" "] * 8 for i in range(8)],
        "Computer Board")
    user_board.print_board()
    computer_board.print_board()
    print(guess())


if __name__ == '__main__':
    new_game()
