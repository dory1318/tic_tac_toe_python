from board import *
from game import *
import unittest

class TestGame(unittest.TestCase):

    def test_move(self):
        game = Game(board.empty_board)
        start = game.make_move(0, "x")
        start = game.make_move(2, "0")
        self.assertEqual (start, ["x", " ", "0", " ", " ", " ", " ", " ", " "])

if __name__ == '__main__':
    unittest.main()
