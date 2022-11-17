"""
A simple Battleship game of a single user playing against computer board.
"""
# Display greetings message to the user
# The player grid displays for the user to commence the game
#   Create Grid
#       Row headers
#       Column headers
#       Grid body
#   Display Grid
# Request user name
# Get user input
# Start turns
# As the user, guess the location of the ship
# Check if duplicate guess
# Check for hit or miss
# Check for win or lose
# At end of game run new game


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


if __name__ == '__main__':
    new_game()
