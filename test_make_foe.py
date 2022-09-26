from unittest import TestCase

import game


class TestMakeFoe(TestCase):
    def test_make_foe_in_zone1_end(self):
        character = game.make_character("jesper", 0, 1)
        character['X'] = 8
        actual = game.make_foe(character)
        expected = {'ATK': 10,
                    'EXP': 90,
                    'HP': 100,
                    'MAX_HP': 100,
                    'NAME': 'Skeleton',
                    'SKILL': 'Bone Missile'}
        self.assertEqual(expected, actual)

    def test_make_foe_in_zone2_entry(self):
        character = game.make_character("jesper", 0, 1)
        character['X'] = 9
        actual = game.make_foe(character)
        expected = {'ATK': 15,
                    'EXP': 150,
                    'HP': 200,
                    'MAX_HP': 200,
                    'NAME': 'Titan',
                    'SKILL': 'Rock Hammer'}
        self.assertEqual(expected, actual)

    def test_make_foe_in_zone2_end(self):
        character = game.make_character("jesper", 0, 1)
        character['X'] = 7
        character['Y'] = 6
        actual = game.make_foe(character)
        expected = {'ATK': 15,
                    'EXP': 150,
                    'HP': 200,
                    'MAX_HP': 200,
                    'NAME': 'Titan',
                    'SKILL': 'Rock Hammer'}
        self.assertEqual(expected, actual)

    def test_make_foe_in_zone3_entry(self):
        character = game.make_character("jesper", 0, 1)
        character['X'] = 7
        character['Y'] = 7
        actual = game.make_foe(character)
        expected = {'ATK': 22,
                    'EXP': 200,
                    'HP': 300,
                    'MAX_HP': 300,
                    'NAME': 'Ruined Baron',
                    'SKILL': 'Death Sentence'}
        self.assertEqual(expected, actual)

    def test_make_foe_in_zone3_end(self):
        character = game.make_character("jesper", 0, 1)
        character['X'] = 9
        character['Y'] = 8
        actual = game.make_foe(character)
        expected = {'ATK': 22,
                    'EXP': 200,
                    'HP': 300,
                    'MAX_HP': 300,
                    'NAME': 'Ruined Baron',
                    'SKILL': 'Death Sentence'}
        self.assertEqual(expected, actual)

    def test_make_foe_in_zone4_boss(self):
        character = game.make_character("jesper", 0, 1)
        character['X'] = 9
        character['Y'] = 9
        actual = game.make_foe(character)
        expected = {'ATK': 25,
                    'EXP': 1000,
                    'HP': 750,
                    'MAX_HP': 750,
                    'NAME': 'Dark Dragon',
                    'SKILL': 'Hellfire'}
        self.assertEqual(expected, actual)
