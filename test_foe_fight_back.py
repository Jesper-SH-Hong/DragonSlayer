from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestFoeFightBack(TestCase):
    def test_foe_fight_back_decreases_HP(self):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        game.foe_fight_back(character, foe)
        actual = character["Current HP"]
        expected = 80
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_fight_back_and_character_has_positive_hp(self, mock_stdout):
        character = game.make_character('Jesper', 0, 1)
        foe = game.make_foe(character)
        game.foe_fight_back(character, foe)
        expected = ("    Skeleton's HP is 100/100\n\n"
                    "    Skeleton casts Bone Missile to you.\n"
                    "    [SYSTEM] Your HP is 80..\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_fight_back_and_character_dies(self, mock_stdout):
        character = game.make_character('Jesper', 0, 1)
        character["Current HP"] = 0
        foe = game.make_foe(character)
        game.foe_fight_back(character, foe)
        expected = ("    Skeleton's HP is 100/100\n\n"
                    "    Skeleton casts Bone Missile to you.\n"
                    "[SYSTEM] Jesper has 0 HP...\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
