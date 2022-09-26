from unittest import TestCase

import game


class TestIsAlive(TestCase):
    def test_is_alive_true(self):
        character = game.make_character('Jesper', 0, 1)
        character['Current HP'] = 10
        actual = game.is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_false(self):
        character = game.make_character('Jesper', 0, 1)
        character['Current HP'] = 0
        actual = game.is_alive(character)
        expected = False
        self.assertEqual(expected, actual)
