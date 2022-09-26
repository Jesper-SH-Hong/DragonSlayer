from unittest import TestCase
from unittest.mock import patch

import game


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_lowest_string_input(self, _):
        actual = game.get_user_choice()
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_highest_string_input(self, _):
        actual = game.get_user_choice()
        expected = "4"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["q"])
    def test_get_user_choice_q(self, _):
        actual = game.get_user_choice()
        expected = "q"
        self.assertEqual(expected, actual)
