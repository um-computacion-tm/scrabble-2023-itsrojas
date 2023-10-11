import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest
from game.scrabble_board import Board
from game.scrabble_objects import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        assert board.is_empty == False

    '''def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = [Tile('F', 1), Tile('a', 1), Tile('c', 1), Tile('u', 1), Tile('l', 1), Tile('t', 1), Tile('a', 1), Tile('d', 1)]
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True'''

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = [Tile('F', 1), Tile('a', 1), Tile('c', 1), Tile('u', 1), Tile('l', 1), Tile('t', 1), Tile('a', 1), Tile('d', 1)]
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == False

    ''' def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = [Tile('F', 1), Tile('a', 1), Tile('c', 1), Tile('u', 1), Tile('l', 1), Tile('t', 1), Tile('a', 1), Tile('d', 1)]
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True '''

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = [Tile('F', 1), Tile('a', 1), Tile('c', 1), Tile('u', 1), Tile('l', 1), Tile('t', 1), Tile('a', 1), Tile('d', 1)]
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == False





    ''' def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        for i, letter in enumerate(word):
            board.grid[location[1] + i][location[0]].add_letter(Tile(letter, 1))
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertFalse(word_is_valid) '''
    
    ''' def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertFalse(word_is_valid)'''
    
    '''class TestBoard:
    def __init__(self, fill_with=None):
        if fill_with is None:
            fill_with = " " * (15 * 15)
        self.grid = [
mport unittest
from game.board import Board

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
        self.assertEqual(cell.is_occupied, True) '''


if __name__ == '__main__':
    unittest.main()
