from unittest import TestCase
import game


class TestFoeIsAlive(TestCase):
    def test_foe_is_alive_dead(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        foe["HP"] = 0
        actual = game.foe_is_alive(foe)
        expected = False
        self.assertEqual(expected, actual)

    def test_foe_is_alive_still_alive(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        foe["HP"] = 1
        actual = game.foe_is_alive(foe)
        expected = True
        self.assertEqual(expected, actual)