import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest

from game.scrabble_objects import Tile
from game.scrabble_board import Board, Cell, SpecialCell

class Board:
    def __init__(self, fill_with=None):
        if fill_with is None:
            fill_with = " " * (15 * 15)
        self.grid = [
            [
                Cell(
                    letter=fill_with[(row * 15) + col],  # Usar el argumento 'letter' en lugar de 'tile'
                    value=1,
                    multiplier=1,
                    multiplier_type=""
                )
                for col in range(15)
            ]
            for row in range(15)
        ]
        self.used_special_cells = set()

    def test_special_cells(self):
        board = Board([])
        for row in range(15):
            for col in range(15):
                cell = board.grid[row][col]
                if cell.multiplier_type:
                    self.assertIsInstance(cell, SpecialCell)
                else:
                    self.assertIsInstance(cell, Cell)

    def test_change_state(self):
        board = Board([])
        row, col = 3, 3
        letter = 'A'
        score = 5

        # Cambia el estado de la celda
        board.change_state(row, col, letter=letter, score=score)

        # Verifica que el estado de la celda haya cambiado correctamente
        cell = board.grid[row][col]
        self.assertEqual(cell.letter, letter)
        self.assertEqual(cell.score, score)
        self.assertEqual(cell.is_occupied, True)

class TestCalculateWord(unittest.TestCase):
    def test_simple(self):
        fill_with = " " * (15 * 15)
        board = Board(fill_with)
        word = [
            board.grid[7][7],  # Celda con letra 'C'
            board.grid[7][8],  # Celda con letra 'A'
            board.grid[7][9],  # Celda con letra 'S'
            board.grid[7][10],  # Celda con letra 'A'
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        fill_with = " " * (15 * 15)
        board = Board(fill_with)
        word = [
            board.grid[7][7],  # Celda con letra 'C'
            board.grid[7][8],  # Celda con letra 'A'
            board.grid[7][9],  # Celda con letra 'S' con multiplicador de letra x2
            board.grid[7][10],  # Celda con letra 'A'
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        fill_with = " " * (15 * 15)
        board = Board(fill_with)
        word = [
            board.grid[7][7],  # Celda con letra 'C'
            board.grid[7][8],  # Celda con letra 'A'
            board.grid[7][9],  # Celda con letra 'S' con multiplicador de palabra x2
            board.grid[7][10],  # Celda con letra 'A'
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 12)


if __name__ == "__main__":
    unittest.main()