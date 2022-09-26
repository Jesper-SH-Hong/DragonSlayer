from unittest import TestCase
from unittest.mock import patch

import game


class TestFoeHitsCharacter(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_foe_hits_character_true(self, _):
        actual = game.foe_hits_character()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_foe_hits_character_false(self, _):
        actual = game.foe_hits_character()
        expected = False
        self.assertEqual(expected, actual)
