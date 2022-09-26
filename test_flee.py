from unittest import TestCase
from unittest.mock import patch

import game


class TestFlee(TestCase):

    @patch('random.randint', side_effect=[1])
    def test_flee_success_with_dmg(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        flee_possible = True
        game.flee(character, foe, flee_possible)
        actual = character["Current HP"]
        expected = 80
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_flee_success_without_dmg(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        flee_possible = True
        game.flee(character, foe, flee_possible)
        actual = character["Current HP"]
        expected = 90
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_flee_success_return_True_when_foe_hits_back(self, _):
        user = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(user)
        flee_possible = True
        actual = game.flee(user, foe, flee_possible)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_flee_success_return_True_when_foe_not_hits_back(self, _):
        user = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(user)
        flee_possible = True
        actual = game.flee(user, foe, flee_possible)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_flee_cannot_flee_from_boss_even_if_flee_possible(self, _):
        player = game.make_character('Jesper', 0, 1)
        player['X'] = 9
        player['Y'] = 9
        foe = game.make_foe(player)
        flee_possible = True
        actual = game.flee(player, foe, flee_possible)
        expected = False
        self.assertEqual(expected, actual)
