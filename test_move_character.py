from unittest import TestCase

import game


class TestMoveCharacter(TestCase):
    def test_move_character_east(self):
        direction = "2"
        character = game.make_character('Jesper', 0, 1)
        game.move_character(direction, character)
        actual = character['X']
        expected = 1
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        direction = "4"
        character = game.make_character('Jesper', 0, 1)
        character['X'] = 3
        character['Y'] = 3
        game.move_character(direction, character)
        actual = character['X']
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_north(self):
        direction = "1"
        character = game.make_character('Jesper', 0, 1)
        character['X'] = 3
        character['Y'] = 3
        game.move_character(direction, character)
        actual = character['Y']
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_south(self):
        direction = "3"
        character = game.make_character('Jesper', 0, 1)
        character['X'] = 3
        character['Y'] = 3
        game.move_character(direction, character)
        actual = character['Y']
        expected = 4
        self.assertEqual(expected, actual)
