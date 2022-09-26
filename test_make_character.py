from unittest import TestCase

import game


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual = game.make_character('Jesper', 3, 3)
        expected = {'ATK': 100,
                    'Class': 'Paladin',
                    'Current HP': 300,
                    'Current_EXP': 0,
                    'Job': 'Sword Master',
                    'Lvl': 3,
                    'Max_EXP': 9999999999,
                    'Max_HP': 300,
                    'Name': 'Jesper',
                    'Skill': 'Trinity Strike',
                    'X': 0,
                    'Y': 0}
        self.assertEqual(expected, actual)

    def test_make_character_with_lowest_user_class_input_0(self):
        actual = game.make_character('Jesper', 0, 1)
        expected = {'ATK': 60,
                    'Class': 'Rogue',
                    'Current HP': 90,
                    'Current_EXP': 0,
                    'Job': 'Thief',
                    'Lvl': 1,
                    'Max_EXP': 100,
                    'Max_HP': 90,
                    'Name': 'Jesper',
                    'Skill': 'Knife Throw',
                    'X': 0,
                    'Y': 0}
        self.assertEqual(expected, actual)

    def test_make_character_with_lowest_user_class_input_1(self):
        actual = game.make_character('Jesper', 1, 2)
        expected = {'ATK': 85,
                    'Class': 'Archer',
                    'Current HP': 180,
                    'Current_EXP': 0,
                    'Job': 'Marksman',
                    'Lvl': 2,
                    'Max_EXP': 210,
                    'Max_HP': 180,
                    'Name': 'Jesper',
                    'Skill': 'Frost Arrow',
                    'X': 0,
                    'Y': 0}
        self.assertEqual(expected, actual)

    def test_make_character_with_lowest_user_class_input_2(self):
        actual = game.make_character('Jesper', 2, 1)
        expected = {'ATK': 55,
                    'Class': 'Wizard',
                    'Current HP': 80,
                    'Current_EXP': 0,
                    'Job': 'Summoner',
                    'Lvl': 1,
                    'Max_EXP': 100,
                    'Max_HP': 80,
                    'Name': 'Jesper',
                    'Skill': 'Thunderbolt',
                    'X': 0,
                    'Y': 0}
        self.assertEqual(expected, actual)

    def test_make_character_with_highest_user_class_input_3(self):
        actual = game.make_character('Jesper', 3, 1)
        expected = {'ATK': 70,
                    'Class': 'Paladin',
                    'Current HP': 100,
                    'Current_EXP': 0,
                    'Job': 'Barbarian',
                    'Lvl': 1,
                    'Max_EXP': 100,
                    'Max_HP': 100,
                    'Name': 'Jesper',
                    'Skill': 'Whirlwind',
                    'X': 0,
                    'Y': 0}

        self.assertEqual(expected, actual)

    def test_make_character_with_highest_lvl_3(self):
        actual = game.make_character('Jesper', 1, 3)
        expected = {'ATK': 120,
                    'Class': 'Archer',
                    'Current HP': 280,
                    'Current_EXP': 0,
                    'Job': 'Sniper',
                    'Lvl': 3,
                    'Max_EXP': 9999999999,
                    'Max_HP': 280,
                    'Name': 'Jesper',
                    'Skill': 'Headshot',
                    'X': 0,
                    'Y': 0}

        self.assertEqual(expected, actual)

    def test_make_character_with_lvl_2(self):
        actual = game.make_character('Jesper', 3, 2)
        expected = {'ATK': 90,
                    'Class': 'Paladin',
                    'Current HP': 200,
                    'Current_EXP': 0,
                    'Job': 'Knight',
                    'Lvl': 2,
                    'Max_EXP': 220,
                    'Max_HP': 200,
                    'Name': 'Jesper',
                    'Skill': 'Reckless Rush',
                    'X': 0,
                    'Y': 0}

        self.assertEqual(expected, actual)

    def test_make_character_with_lowest_lvl_1(self):
        actual = game.make_character('Jesper', 1, 1)
        expected = {'ATK': 65,
                    'Class': 'Archer',
                    'Current HP': 85,
                    'Current_EXP': 0,
                    'Job': 'Hunter',
                    'Lvl': 1,
                    'Max_EXP': 100,
                    'Max_HP': 85,
                    'Name': 'Jesper',
                    'Skill': 'Quick Shot',
                    'X': 0,
                    'Y': 0}

        self.assertEqual(expected, actual)
