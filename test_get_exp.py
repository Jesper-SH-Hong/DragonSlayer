from unittest import TestCase
import game


class TestGetExp(TestCase):
    def test_get_exp_zone1(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.FOES()[1]
        game.get_exp(character, foe)
        expected = character["Current_EXP"]
        actual = 90
        self.assertEqual(expected, actual)

    def test_get_exp_zone2(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.FOES()[2]
        game.get_exp(character, foe)
        expected = character["Current_EXP"]
        actual = 150
        self.assertEqual(expected, actual)

    def test_get_exp_zone3(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.FOES()[3]
        game.get_exp(character, foe)
        expected = character["Current_EXP"]
        actual = 200
        self.assertEqual(expected, actual)