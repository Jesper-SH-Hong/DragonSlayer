from unittest import TestCase

import game


class TestBlessForFinalBattle(TestCase):
    def test_bless_for_final_battle(self):
        character = game.make_character('Jesper', 0, 1)
        game.bless_for_final_battle(character)
        actual = character["Current HP"]
        expected = character["Max_HP"]
        self.assertEqual(expected, actual)
