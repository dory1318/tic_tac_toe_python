class Board():
    def __init__(self):
        self.empty_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board(self):
        print(self.empty_board[0], "|", self.empty_board[1], "|", self.empty_board[2])
        print("__________")
        print(self.empty_board[3], "|", self.empty_board[4], "|", self.empty_board[5])
        print("__________")
        print(self.empty_board[6], "|", self.empty_board[7], "|", self.empty_board[8])


board = Board()
board.print_board()
