from board import *

class Game():
    def __init__(self, board):
        self.new_board = board

    def make_move(self, move, shape):
        self.new_board[move] = shape
        return self.new_board

    def field_is_taken(self, move):
        if self.new_board[move] != " ":
            return True
        else:
            return False
