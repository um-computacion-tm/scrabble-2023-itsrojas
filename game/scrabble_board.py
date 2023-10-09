from game.scrabble_objects import Tile
from game.scrabble_cells import Cell, SpecialCell
import unittest

class Board:
    def __init__(self, fill_with=None):
        if fill_with is None:
            fill_with = " " * (15 * 15)
        self.grid = [
            [
                Cell(
                    letter=fill_with[(row * 15) + col] if fill_with[(row * 15) + col] != " " else None,
                    value=1
                )
                for col in range(15)
            ]
            for row in range(15)
        ]
        self.used_special_cells = set()

    def define_special_cells(self):
        special_cells = {
            (0, 0): ('x3_word', 'W3'), (0,7): ('x3_word', 'W3'), (0,14): ('x3_word', 'W3'), (7,0): ('x3_word', 'W3'), (7,14): ('x3_word', 'W3'), (14,0): ('x3_word', 'W3'), (14,7): ('x3_word', 'W3'), (14,14): ('x3_word', 'W3'),
            (1,5): ('x3_letter', 'L3'), (1,9): ('x3_letter', 'L3'), (5,1): ('x3_letter', 'L3'),(5,5): ('x3_letter', 'L3'),(5,9): ('x3_letter', 'L3'), (5,13): ('x3_letter', 'L3'), (9,1): ('x3_letter', 'L3'),  (9,5): ('x3_letter', 'L3'),
            (9,9): ('x3_letter', 'L3'), (9,13): ('x3_letter', 'L3'), (13,5): ('x3_letter', 'L3'), (13,9): ('x3_letter', 'L3'),
            (1,1): ('x2_word', 'W2'), (2,2): ('x2_word', 'W2'), (3,3): ('x2_word', 'W2'), (4,4): ('x2_word', 'W2'), (4,10): ('x2_word', 'W2'), (3,11): ('x2_word', 'W2'), (2,12): ('x2_word', 'W2'), (1,13): ('x2_word', 'W2'),
            (13,1): ('x2_word', 'W2'), (12,2): ('x2_word', 'W2'), (11,3): ('x2_word', 'W2'), (10,4): ('x2_word', 'W2'), (10,10): ('x2_word', 'W2'), (11,11): ('x2_word', 'W2'), (12,12): ('x2_word', 'W2'), (13,13): ('x2_word', 'W2'), 
            (0,3): ('x2_letter', 'L2'), (0,12): ('x2_letter', 'L2'), (2,6): ('x2_letter', 'L2'), (2,8): ('x2_letter', 'L2'), (3,0): ('x2_letter', 'L2'), (3,7): ('x2_letter', 'L2'), (3,14): ('x2_letter', 'L2'), (6,2): ('x2_letter', 'L2'),
            (6,6): ('x2_letter', 'L2'), (6,8): ('x2_letter', 'L2'), (6,12): ('x2_letter', 'L2'), (7,3): ('x2_letter', 'L2'), (7,11): ('x2_letter', 'L2'), (8,2): ('x2_letter', 'L2'), (8,6): ('x2_letter', 'L2'), (8,8): ('x2_letter', 'L2'),
            (8,12): ('x2_letter', 'L2'), (11,0): ('x2_letter', 'L2'), (11,7): ('x2_letter', 'L2'), (11,14): ('x2_letter', 'L2'), (12,6): ('x2_letter', 'L2'), (12,8): ('x2_letter', 'L2'), (14,3): ('x2_letter', 'L2'), (14,11): ('x2_letter', 'L2')
        }
        for row, col in special_cells:
            multiplier_type, icon = special_cells[(row, col)]
            self.grid[row][col] = SpecialCell(
                multiplier=self.get_multiplier(row, col),  # Ajusta esta línea
                multiplier_type=multiplier_type,
                icon=icon,
            )
    
    def get_multiplier(self, row, col):
        # Implementa la lógica para obtener el multiplicador en función de la posición (row, col)
        # Por ejemplo, puedes implementar aquí las reglas del juego Scrabble.
        # Aquí proporciono un ejemplo simple en el que se devuelven multiplicadores predeterminados.
        if (row, col) in [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]:
            return 3  # Multiplicador de palabra x3 en las esquinas
        elif (row, col) in [(1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10),
                            (10, 4), (11, 3), (12, 2), (13, 1), (10, 10), (11, 11), (12, 12), (13, 13)]:
            return 2  # Multiplicador de palabra x2 en las posiciones indicadas
        elif (row, col) in [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13),
                            (13, 5), (13, 9)]:
            return 3  # Multiplicador de letra x3 en las posiciones indicadas
        elif (row, col) in [(0, 3), (0, 12), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2),
                            (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12),
                            (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]:
            return 2  # Multiplicador de letra x2 en las posiciones indicadas
        else:
            return 1


    def validate_word_inside_board(self, word, location, orientation):
        row, col = location
        if orientation == "H":
            return col + len(word) <= 15
        elif orientation == "V":
            return row + len(word) <= 15
        return False

    def calculate_word_value(self, word):
        value = 0
        multiplier_word = 1
        for cell in word:
            if cell.is_occupied:
                cell_value = cell.calculate_value()
                if cell.multiplier_type == "letter":
                    cell_value *= cell.multiplier
                value += cell_value
                if cell.multiplier_type == "word":
                    multiplier_word *= cell.multiplier
        return value * multiplier_word

    def place_word(self, word, location, orientation):
        row, col = location
        for letter in word:
            self.grid[row][col].add_letter(letter)
            if orientation == "H":
                col += 1
            elif orientation == "V":
                row += 1
        self.change_state(row, col, letter=word, score=0)

    def change_state(self, row, col, letter=None, score=0):
        cell = self.grid[row][col]
        cell.letter = letter
        cell.score = score
        cell.is_occupied = True


