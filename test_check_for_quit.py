from unittest import TestCase

import game


class TestCheckForQuit(TestCase):
    def test_check_for_quit_is_true(self):
        direction = "q"
        actual = game.check_for_quit(direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_for_quit_is_false(self):
        direction = "2"
        actual = game.check_for_quit(direction)
        expected = False
        self.assertEqual(expected, actual)
