from unittest import TestCase
from unittest.mock import patch

import game


class TestGetUserName(TestCase):
    @patch('builtins.input', side_effect=["Jesper"])
    def test_get_user_name(self, _):
        actual = game.get_user_name()
        expected = "Jesper"
        self.assertEqual(expected, actual)
