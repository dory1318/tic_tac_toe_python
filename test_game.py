from board import *
from game import *
import unittest
import pytest

class TestGame(unittest.TestCase):

    def test_move(self):
        game = Game(board.empty_board)
        game.make_move(0, "x")
        self.assertEqual (game.new_board[0], "x")

    def test_move_to_occupied_field(self):
        game = Game(board.empty_board)
        with pytest.raises(Exception) as excinfo:
            game.make_move(0, "x")
        assert str(excinfo.value) == "Sorry, that field is already taken, choose another one!"

    def test_taken_field(self):
        game = Game(board.empty_board)
        taken = game.field_is_taken(0)
        self.assertEqual (taken, True)

    def test_not_taken_field(self):
        game = Game(board.empty_board)
        empty = game.field_is_taken(1)
        self.assertEqual (empty, False)

    def test_board_is_full(self):
        game = Game(["x", "x", "0", "x", "0", "x", "0", "0", "x"])
        self.assertEqual (game.full_board(), True)

    def test_board_isnt_full(self):
        game = Game([" ", "x", "0", "x", "0", "x", "0", "0", "x"])
        self.assertEqual (game.full_board(), False)

    def test_x_won(self):
        game = Game(board.empty_board)
        game.make_move(3, "x")
        game.make_move(6, "x")
        self.assertEqual (game.x_won(), True)

    def test_0_won(self):
        game = Game(board.empty_board)
        game.make_move(2, "o")
        game.make_move(5, "o")
        game.make_move(8, "o")
        self.assertEqual (game.o_won(), True)

if __name__ == '__main__':
    unittest.main()
