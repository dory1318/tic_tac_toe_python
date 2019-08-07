import numpy as np

class Game():
    ROWS = 3
    COLUMNS = 3
    def __init__(self):
        self.new_board = np.zeros((self.ROWS, self.COLUMNS), dtype=int)

    def make_move(self, column_coordinate, row_coordinate, player):
        if self.field_is_taken(column_coordinate, row_coordinate):
            raise Exception("Sorry, that field is already taken, choose another one!")
        else:
            self.new_board[column_coordinate][row_coordinate] = player
            return self.new_board

    def field_is_taken(self, column_coordinate, row_coordinate):
        if self.new_board[column_coordinate][row_coordinate] != 0:
            return True
        else:
            return False

    def full_board(self):
        if not 0 in (self.new_board[0] and self.new_board[1] and self.new_board[2]):
            return True
        else:
            return False

    def winner(self):
        if (self.new_board[0][0] == self.new_board[0][1] and self.new_board[0][1] == self.new_board[0][2] and self.new_board[0][1]):
            return self.new_board[0][1]
        if (self.new_board[1][0] == self.new_board[1][1] and self.new_board[1][1] == self.new_board[1][2] and self.new_board[1][1]):
            return self.new_board[1][1]
        if (self.new_board[2][0] == self.new_board[2][1] and self.new_board[2][1] == self.new_board[2][2] and self.new_board[2][1]):
            return self.new_board[2][1]
        if (self.new_board[0][0] == self.new_board[1][0] and self.new_board[1][0] == self.new_board[2][0] and self.new_board[1][0]):
            return self.new_board[1][0]
        if (self.new_board[0][1] == self.new_board[1][1] and self.new_board[1][1] == self.new_board[2][1] and self.new_board[1][1]):
            return self.new_board[1][1]
        if (self.new_board[0][2] == self.new_board[1][2] and self.new_board[1][2] == self.new_board[2][2] and self.new_board[2][1]):
            return self.new_board[2][1]
        if (self.new_board[0][0] == self.new_board[1][1] and self.new_board[1][1] == self.new_board[2][2] and self.new_board[1][1]):
            return self.new_board[1][1]
        if (self.new_board[0][2] == self.new_board[1][1] and self.new_board[1][1] == self.new_board[2][0] and self.new_board[1][1]):
            return self.new_board[1][1]
        else:
            return None
