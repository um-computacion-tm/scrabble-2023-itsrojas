import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest

from game.scrabble_board import Board
from game.scrabble_cells import Cell
from game.scrabble_objects import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 3)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 1)),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)  # Utiliza la función importada
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 3)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)  # Utiliza la función importada
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 3)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)  # Utiliza la función importada
        self.assertEqual(value, 12)

    def test_with_letter_word_multiplier(self):
        board = Board()
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 3)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)  # Utiliza la función importada
        self.assertEqual(value, 24)

    '''def test_with_letter_word_multiplier_no_active(self):
        # QUE HACEMOS CON EL ACTIVE ????
        board = Board()
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 3)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)  # Utiliza la función importada
        self.assertEqual(value, 6)'''

if __name__ == '__main__':
    unittest.main()
