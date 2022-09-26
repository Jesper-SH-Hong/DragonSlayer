from unittest import TestCase
from unittest.mock import patch

import game


class TestFoeFlee(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_foe_flee_true(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        actual = game.foe_flee(foe)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[2])
    def test_foe_flee_false_due_to_randint(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        actual = game.foe_flee(foe)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1])
    def test_foe_flee_false_for_boss_even_if_meet_randint(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        foe['NAME'] = 'Dark Dragon'
        actual = game.foe_flee(foe)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[2])
    def test_foe_flee_false_for_boss_and_fail_randint(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        foe['NAME'] = 'Dark Dragon'
        actual = game.foe_flee(foe)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1])
    def test_foe_flee_false_foe_is_already_dead(self, _):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        foe['HP'] = 0
        actual = game.foe_flee(foe)
        expected = False
        self.assertEqual(actual, expected)
