from unittest import TestCase
import game


class TestNotEnoughCurrentExpForLvlUp(TestCase):
    def test_not_enough_current_exp_for_lvl_up_true(self):
        character = game.make_character('Jesper', 0, 1)
        character["Current_EXP"] = 99
        actual = game.not_enough_current_exp_for_lvl_up(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_not_enough_current_exp_for_lvl_up_False_lv1(self):
        character = game.make_character('Jesper', 0, 1)
        character["Current_EXP"] = 100
        actual = game.not_enough_current_exp_for_lvl_up(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_not_enough_current_exp_for_lvl_up_True_lv2(self):
        character = game.make_character('Jesper', 0, 2)
        character["Current_EXP"] = 179
        actual = game.not_enough_current_exp_for_lvl_up(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_not_enough_current_exp_for_lvl_up_False_lv2(self):
        character = game.make_character('Jesper', 0, 2)
        character["Current_EXP"] = 180
        actual = game.not_enough_current_exp_for_lvl_up(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_not_enough_current_exp_for_lvl_up_True_lv3(self):
        character = game.make_character('Jesper', 0, 3)
        character["Current_EXP"] = 9999999998
        actual = game.not_enough_current_exp_for_lvl_up(character)
        expected = True
        self.assertEqual(expected, actual)