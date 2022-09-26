from unittest import TestCase
from unittest.mock import patch
import game


class TestCheckForFoes(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_check_for_foes_true(self, _):
        character = game.make_character('Jesper', 0, 1)
        actual = game.check_for_foes(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_check_for_foes_false(self, _):
        character = game.make_character('Jesper', 0, 1)
        actual = game.check_for_foes(character)
        expected = False
        self.assertEqual(expected, actual)
