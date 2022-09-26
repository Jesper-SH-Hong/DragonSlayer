from unittest import TestCase
import unittest.mock
import io

import game


class TestDisplayUserClass(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_user_class(self, mock_stdout):
        game.display_user_class()
        expected = ("1, Rogue:      Faster growth\n"
                    "2, Archer:     Balanced stat\n"
                    "3, Wizard:     Low HP, powerful skill\n"
                    "4, Paladin:    Tank. great HP\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
