from unittest import TestCase

import game


class TestPaint(TestCase):
    def test_paint_input_is_1(self):
        actual = game.paint("1")
        expected = "☆"
        self.assertEqual(expected, actual)

    def test_paint_input_is_2(self):
        actual = game.paint("2")
        expected = "★"
        self.assertEqual(expected, actual)
