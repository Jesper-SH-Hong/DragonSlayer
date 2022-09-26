from unittest import TestCase
import unittest.mock
import game
import io


class TestDisplayMap(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map(self, mock_stdout):
        board = game.make_board(3, 3)
        character = game.make_character('jes', 0, 1)
        game.display_map(board, character)
        expected = ".\n.\n.\n[X][ ][ ]\n[ ][ ][ ]\n[ ][ ][*]\n"
        self.assertEqual(expected, mock_stdout.getvalue())
