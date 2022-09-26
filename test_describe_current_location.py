from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_stdout):
        board = game.make_board(3, 3)
        character = game.make_character('Jesper', 1, 1)
        board[(0, 0)] = "Ruins"
        game.describe_current_location(board, character)
        expected = "Great! You are in the Ruins\n"
        self.assertEqual(expected, mock_stdout.getvalue())
