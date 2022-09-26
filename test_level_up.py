from unittest import TestCase

import game


class TestLevelUp(TestCase):
    def test_level_up_from_lvl1(self):
        player = game.make_character("Jes", 3, 1)
        player['X'] = 5
        player['Y'] = 5
        player["Current_EXP"] = 100
        actual = game.level_up(player, 3)
        expected = {'ATK': 90,
                    'Class': 'Paladin',
                    'Current HP': 200,
                    'Current_EXP': 0,
                    'Job': 'Knight',
                    'Lvl': 2,
                    'Max_EXP': 220,
                    'Max_HP': 200,
                    'Name': 'Jes',
                    'Skill': 'Reckless Rush',
                    'X': 5,
                    'Y': 5}
        self.assertEqual(expected, actual)

    def test_level_up_from_lvl2(self):
        player = game.make_character("Jes", 3, 2)
        player['X'] = 5
        player['Y'] = 5
        player["Current_EXP"] = 300
        actual = game.level_up(player, 3)
        expected = {'ATK': 100,
                    'Class': 'Paladin',
                    'Current HP': 300,
                    'Current_EXP': 0,
                    'Job': 'Sword Master',
                    'Lvl': 3,
                    'Max_EXP': 9999999999,
                    'Max_HP': 300,
                    'Name': 'Jes',
                    'Skill': 'Trinity Strike',
                    'X': 5,
                    'Y': 5}
        self.assertEqual(expected, actual)

    def test_level_up_not_enough_exp(self):
        player = game.make_character("Jes", 3, 1)
        player['X'] = 5
        player['Y'] = 5
        player["Current_EXP"] = 20
        actual = game.level_up(player, 3)
        expected = {'ATK': 70,
                    'Class': 'Paladin',
                    'Current HP': 100,
                    'Current_EXP': 20,
                    'Job': 'Barbarian',
                    'Lvl': 1,
                    'Max_EXP': 100,
                    'Max_HP': 100,
                    'Name': 'Jes',
                    'Skill': 'Whirlwind',
                    'X': 5,
                    'Y': 5}
        self.assertEqual(expected, actual)
