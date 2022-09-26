from unittest import TestCase
import game


class TestReduceFoeHP(TestCase):
    def test_reduce_foe_hp_foe_in_zone1(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.FOES()[1]
        game.reduce_foe_hp(foe, character)
        actual = foe["HP"]
        expected = 40
        self.assertEqual(expected, actual)

    def test_reduce_foe_hp_foe_in_zone2(self):
        character = game.make_character('Jesper', 0, 2)
        foe = game.FOES()[2]
        game.reduce_foe_hp(foe, character)
        actual = foe["HP"]
        expected = 115

        self.assertEqual(expected, actual)

    def test_reduce_foe_hp_foe_in_zone3(self):
        character = game.make_character('Jesper', 0, 3)
        foe = game.FOES()[3]
        game.reduce_foe_hp(foe, character)
        actual = foe["HP"]
        expected = 190
        self.assertEqual(expected, actual)

    def test_reduce_foe_hp_boss(self):
        character = game.make_character('Jesper', 0, 2)
        foe = game.BOSS()
        game.reduce_foe_hp(foe, character)
        actual = foe["HP"]
        expected = 665

        self.assertEqual(expected, actual)