from unittest import TestCase

import game


class TestValidateMove(TestCase):
    def test_validate_move_north_fail(self):
        board = game.make_board(3, 3)
        character = game.make_character("Jesper", 0, 1)
        direction = "1"
        character['X'] = 0
        character['Y'] = 0
        actual = game.validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_south_fail(self):
        board = game.make_board(3, 3)
        character = game.make_character("Jesper", 0, 1)
        direction = "3"
        character['X'] = 0
        character['Y'] = 3
        actual = game.validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_west_fail(self):
        board = game.make_board(2, 2)
        character = game.make_character("Jesper", 0, 1)
        direction = "4"
        character['X'] = 0
        character['Y'] = 2
        actual = game.validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_east_fail(self):
        board = game.make_board(4, 4)
        character = game.make_character("Jesper", 0, 1)
        direction = "2"
        character['X'] = 4
        character['Y'] = 0
        actual = game.validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_success(self):
        board = game.make_board(5, 5)
        character = game.make_character("Jesper", 0, 1)
        direction = "1"
        character['X'] = 2
        character['Y'] = 2
        actual = game.validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)
