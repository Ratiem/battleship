"""
A simple Battleship game of a single user playing against computer board.
"""
import random

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

    def add_ships(self):
        """
        Populates a board with 5 randomly placed ships
        """
        for i in range(5):
            self.x_row = random.randint(0, 7)
            self.y_column = random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row = random.randint(0, 7)
                self.y_column = random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self

    def calculate_sunk_ships(self):
        """"
        Calculates the number of sunken ships, this is indicated by 'X'
        """
        sunk_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    sunk_ships += 1
        return sunk_ships


def guess():
    """
    Get user input
    """
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


def play_game(user, computer):
    """
    Sets the turns for the user and board game to display
    """
    turns = 10
    while turns > 0:
        user.print_board()
        turns -= 1
        user_x_row, user_y_column = guess()
        while user.board[user_x_row][user_y_column] in "-X":
            print("You have already guessed this one!")
            user_x_row, user_y_column = guess()
        if computer.board[user_x_row][user_y_column] == "X":
            print("You sunk 1 of my battleships!")
            user.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed my battleship!")
            user.board[user_x_row][user_y_column] = "-"
        if user.calculate_sunk_ships() == 5:
            print("You have hit all 5 battleships!")
            break
    if user.calculate_sunk_ships() == 5:
        print("You win!")
    else:
        print("You have run out of turns, you lose!")


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
