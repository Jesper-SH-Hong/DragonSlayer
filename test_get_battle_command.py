from unittest import TestCase
from unittest.mock import patch
import game


class TestGetBattleCommand(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_get_battle_command_1(self, _):
        actual = game.get_battle_command()
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[2])
    def test_get_battle_command_2(self, _):
        actual = game.get_battle_command()
        expected = 2
        self.assertEqual(expected, actual)