from unittest import TestCase
from unittest.mock import patch

import game


class TestCheckFleeChance(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_check_flee_chance_true(self, _):
        actual = game.check_flee_chance()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_check_flee_chance_false(self, _):
        actual = game.check_flee_chance()
        expected = False
        self.assertEqual(expected, actual)
