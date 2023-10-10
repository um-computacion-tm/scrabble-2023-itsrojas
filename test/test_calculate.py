import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest

from game.scrabble_board import Board
from game.scrabble_cells import Cell
from game.scrabble_objects import Tile

'''class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        word = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word[2].multiplier = 2
        word[2].multiplier_type = 'letter'
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word[2].multiplier = 2
        word[2].multiplier_type = 'word'
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 12)

    def test_with_letter_word_multiplier(self):
        word = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word[0].multiplier = 3
        word[0].multiplier_type = 'letter'
        word[2].multiplier = 2
        word[2].multiplier_type = 'word'
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 24)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word[0].multiplier = 3
        word[0].multiplier_type = 'letter'
        word[2].multiplier = 2
        word[2].multiplier_type = 'word'
        # word[0].active = False  # Comenta esto si no hay un atributo 'active' en Tile
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 6)

if __name__ == '__main__':
    unittest.main() '''
