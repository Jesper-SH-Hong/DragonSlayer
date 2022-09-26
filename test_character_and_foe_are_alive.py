from unittest import TestCase
import game


class TestCharacterAndFoeAreAlive(TestCase):
    def test_character_and_foe_are_alive(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        actual = game.character_and_foe_are_alive(character, foe)
        expected = True
        self.assertEqual(expected, actual)

    def test_character_and_foe_are_alive_only_character_alive(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        foe["HP"] = 0
        actual = game.character_and_foe_are_alive(character, foe)
        expected = False
        self.assertEqual(expected, actual)

    def test_character_and_foe_are_alive_only_foe_alive(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        character["Current HP"] = 0
        actual = game.character_and_foe_are_alive(character, foe)
        expected = False
        self.assertEqual(expected, actual)

    def test_character_and_foe_are_alive_both_dead(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        character["Current HP"] = 0
        foe["HP"] = 0
        actual = game.character_and_foe_are_alive(character, foe)
        expected = False
        self.assertEqual(expected, actual)