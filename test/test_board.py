import unittest

from game.scrabble_objects import Tile
from game.scrabble_board import Board, Cell, SpecialCell

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
    
    def test_special_cells(self):
        board = Board()
        special_cells_positions = [
            (0, 0), (0, 7), (0, 14),
            (7, 0), (7, 14),
            (14, 0), (14, 7), (14, 14),
            (1, 5), (1, 9), (5, 1),
            (5, 5), (5, 9), (5, 13),
            (9, 1), (9, 5), (9, 9), (9, 13),
            (13, 5), (13, 9),
            (1, 1), (2, 2), (3, 3), (4, 4),
            (4, 10), (3, 11), (2, 12), (1, 13),
            (13, 1), (12, 2), (11, 3), (10, 4),
            (10, 10), (11, 11), (12, 12), (13, 13),
            (0, 3), (0, 12), (2, 6), (2, 8),
            (3, 0), (3, 7), (3, 14), (6, 2),
            (6, 6), (6, 8), (6, 12), (7, 3),
            (7, 11), (8, 2), (8, 6), (8, 8),
            (8, 12), (11, 0), (11, 7), (11, 14),
            (12, 6), (12, 8), (14, 3), (14, 11)
        ]
        
        for row in range(15):
            for col in range(15):
                if (row, col) in special_cells_positions:
                    self.assertIsInstance(board.grid[row][col], SpecialCell)
                else:
                    self.assertIsInstance(board.grid[row][col], Cell)

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )
    
    def test_with_word_multiplayer(self):
        cell = Cell
        word = [
            cell(multiplier = 3,
                 multiplier_type='letter',
                 ),

        ]

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 3)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 1)),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)  # Llama al método de la instancia de Board
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
        value = board.calculate_word_value(word)  # Llama al método de la instancia de Board
        self.assertEqual(value, 7)

if __name__ == '__main__':
    unittest.main()