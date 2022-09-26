from unittest import TestCase
import unittest.mock
import io

import game


class TestDisplayCommand(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_command(self, mock_stdout):
        character = game.make_character('Jesper', 0, 1)
        game.display_command(character)
        expected = ("Jesper, enter your next action: \n"
                    " [1], Attack\n"
                    " [2], Flee\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
