from unittest import TestCase
from unittest.mock import patch

import game


class TestGetUserClass(TestCase):
    @patch('builtins.input', side_effect=["4"])
    def test_get_user_class(self, _):
        actual = game.get_user_class()
        expected = 3
        self.assertEqual(expected, actual)
