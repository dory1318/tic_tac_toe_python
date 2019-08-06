from board import *

class Game():
    def __init__(self, board):
        self.new_board = board

    def make_move(self, move, shape):
        if self.field_is_taken(move):
            raise Exception("Sorry, that field is already taken, choose another one!")
        else:
            self.new_board[move] = shape
            return self.new_board

    def field_is_taken(self, move):
        if self.new_board[move] != " ":
            return True
        else:
            return False

    def full_board(self):
        if not " " in self.new_board:
            return True
        else:
            return False

    def x_won(self):
        if(
            (self.new_board[0] == "x" and self.new_board[1] == "x" and self.new_board[2] == "x") or
            (self.new_board[3] == "x" and self.new_board[4] == "x" and self.new_board[5] == "x") or
            (self.new_board[6] == "x" and self.new_board[7] == "x" and self.new_board[8] == "x") or
            (self.new_board[0] == "x" and self.new_board[3] == "x" and self.new_board[6] == "x") or
            (self.new_board[1] == "x" and self.new_board[4] == "x" and self.new_board[7] == "x") or
            (self.new_board[2] == "x" and self.new_board[5] == "x" and self.new_board[8] == "x") or
            (self.new_board[0] == "x" and self.new_board[4] == "x" and self.new_board[8] == "x") or
            (self.new_board[2] == "x" and self.new_board[4] == "x" and self.new_board[6] == "x")
            ):
            return True

    def o_won(self):
        if(
            (self.new_board[0] == "o" and self.new_board[1] == "o" and self.new_board[2] == "o") or
            (self.new_board[3] == "o" and self.new_board[4] == "o" and self.new_board[5] == "o") or
            (self.new_board[6] == "o" and self.new_board[7] == "o" and self.new_board[8] == "o") or
            (self.new_board[0] == "o" and self.new_board[3] == "o" and self.new_board[6] == "o") or
            (self.new_board[1] == "o" and self.new_board[4] == "o" and self.new_board[7] == "o") or
            (self.new_board[2] == "o" and self.new_board[5] == "o" and self.new_board[8] == "o") or
            (self.new_board[0] == "o" and self.new_board[4] == "o" and self.new_board[8] == "o") or
            (self.new_board[2] == "o" and self.new_board[4] == "o" and self.new_board[6] == "o")
            ):
            return True
