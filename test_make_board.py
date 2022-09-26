from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):
    @patch('random.choices', return_value=["Swamp"])
    def test_make_board(self, _):
        expected = {(0, 0): "Swamp"}
        actual = make_board(1, 1)
        self.assertEqual(expected, actual)
