"""
A simple Battleship game of a single user playing against computer board.
"""

# import random



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

    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        """
        Columns will be represented by letters while
        rows will be represented by numbers
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        """
        Print the board
        """
        print("  A B C D E F G H")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


# class Battleship:
#     def __init__(self, board):
#         self.board = board

#     def add_ships(self):
#         for i in range(5):
#             self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
#             while self.board[self.x_row][self.y_column] == "X":
#                 self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
#             self.board[self.x_row][self.y_column] = "X"
#         return self.board

#     def populate_sunk_ships(self):
#         sunk_ships = 0
#         for row in self.board:
#             for column in row:
#                 if column == "X":
#                     sunk_ships += 1
#         return sunk_ships

    def guess(self):
        try:
            x_row = input("Enter the row number of the ship: ")
            while x_row not in '12345678':
                print("Not a valid choice, please enter a valid row number")
            x_row = input("Enter the row number of the ship: ")

            y_column = input("Enter the column letter of the ship ").upper()
            while y_column not in 'ABCDEFGH':
                print("Not a valid choice, please enter a valid column letter")
            y_column = input("Enter the column letter of the ship ").upper()
            return int(x_row) - 1, ShipBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.guess


# def new_game():
#     computer_board = ShipBoard([[" "] * 8 for i in range(8)])
#     user_board = ShipBoard([[" "] * 8 for i in range(8)])
#     Battleship.add_ships(computer_board)

#     turns = 10
#     while turns > 0:
#         ShipBoard.print_board(user_board)
#         user_x_row, user_y_column = guess()
#         while user_board.board[user_x_row][user_y_column] == "-" or user_board.board[user_x_row][user_y_column] == "X":
#             print("You have already guessed this one")
#         user_x_row, user_y_column = guess()
#         if computer_board.board[user_x_row][user_y_column] == "X":
#             print("You sunk 1 of my battleship!")
#         user_board.board[user_x_row][user_y_column] = "X"
#     else:
#         print("You missed my battleship!")
#         user_board.board[user_x_row][user_y_column] = "-"
#     if Battleship.populate_sunk_ships(user_board) == 5:
#         print("You hit all 5 battleships!")


#     else:
#         turns -= 1
#     print(f"You have {turns} turns left")
#     if turns == 0:
#         print("Sorry you have run out of turns")
#         ShipBoard.print_board(user_board)

def new_game():
    """
    Create a new game
    """
    display_greetings_message()
    user_board = ShipBoard([[" "] * 8 for i in range(8)])
    user_board.print_board()


if __name__ == '__main__':
    new_game()
