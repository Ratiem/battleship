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
        letters_to_numbers = ["A": 0]

    def print_board(self):
        for row in self.board:
            print(" ".join(row))