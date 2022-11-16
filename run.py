import random

""" 
A simple Battleship game
"""

class ShipBoard:
    """
    Main Board class
    """

    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        """
        For every Letter that will be declared, it will be equivalent to a number.
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
        print("-" * 50)
        print("Welcome to the Battleships Game!!")
        print("-" * 50)