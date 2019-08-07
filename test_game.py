from game import *
import unittest
import pytest

class TestGame(unittest.TestCase):

    def test_move(self):
        game = Game()
        game.make_move(0, 0, 1)
        self.assertEqual (game.new_board[0][0], 1)

    def test_move_to_occupied_field(self):
        game = Game()
        game.make_move(0, 0, 1)
        with pytest.raises(Exception) as excinfo:
            game.make_move(0, 0, 1)
        assert str(excinfo.value) == "Sorry, that field is already taken, choose another one!"

    def test_taken_field(self):
        game = Game()
        game.make_move(0, 0, 1)
        taken = game.field_is_taken(0, 0)
        self.assertEqual (taken, True)

    def test_not_taken_field(self):
        game = Game()
        game.make_move(0, 0, 1)
        empty = game.field_is_taken(0, 1)
        self.assertEqual (empty, False)

    def test_board_is_full(self):
        game = Game()
        game.new_board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual (game.full_board(), True)

    def test_board_isnt_full(self):
        game = Game()
        game.new_board = [[1, 1, 1], [1, 1, 1], [0, 1, 1]]
        self.assertEqual (game.full_board(), False)

    def test_winner(self):
        game = Game()
        game.new_board = [[1, 1, 1], [0, 0, 1], [0, 1, 0]]
        self.assertEqual (game.winner(), 1)

    def test_winner_again(self):
        game = Game()
        game.new_board = [[0, -1, 0], [0, -1, 0], [0, -1, 0]]
        self.assertEqual (game.winner(), -1)

    def test_empty_board_is_not_winner(self):
        game = Game()
        self.assertEqual (game.winner(), None)

if __name__ == '__main__':
    unittest.main()
