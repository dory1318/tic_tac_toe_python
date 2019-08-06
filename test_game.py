from board import *
from game import *
import unittest
import pytest

class TestGame(unittest.TestCase):

    def test_move(self):
        game = Game(board.empty_board)
        new_board = game.make_move(0, "x")
        new_board = game.make_move(2, "0")
        self.assertEqual (new_board, ["x", " ", "0", " ", " ", " ", " ", " ", " "])

    def test_move_to_occupied_field(self):
        game = Game(board.empty_board)
        with pytest.raises(Exception) as excinfo:
            game.make_move(2, "0")
        assert str(excinfo.value) == "Sorry, that field is already taken, choose another one!"

    def test_taken_field(self):
        game = Game(board.empty_board)
        taken = game.field_is_taken(0)
        self.assertEqual (taken, True)

    def test_not_taken_field(self):
        game = Game(board.empty_board)
        empty = game.field_is_taken(1)
        self.assertEqual (empty, False)

if __name__ == '__main__':
    unittest.main()
