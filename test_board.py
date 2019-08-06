from board import *
import unittest

class TestBoard(unittest.TestCase):

    def test_board(self):
        board = Board()
        start = board.empty_board
        self.assertEqual (start, [" ", " ", " ", " ", " ", " ", " ", " ", " "])

if __name__ == '__main__':
    unittest.main()
