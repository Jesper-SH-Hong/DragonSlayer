from unittest import TestCase

import game


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_true(self):
        board = game.make_board(10, 10)
        character = game.make_character('Jesper', 0, 1)
        character['X'] = 9
        character['Y'] = 9
        actual = game.check_if_goal_attained(board, character)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_not_yet(self):
        board = game.make_board(10, 10)
        character = game.make_character('Jesper', 0, 1)
        character['X'] = 8
        character['Y'] = 9
        actual = game.check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(expected, actual)