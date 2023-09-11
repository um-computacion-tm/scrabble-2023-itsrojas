from game.scrabble_objects import Tile
import unittest

class Board:
    def __init__(self):
        self.grid = [
            [Cell(multiplier=1, multiplier_type='') for _ in range(15)]  
            for _ in range(15)
        ]
        self.define_special_cells()

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
            self.grid[row][col] = SpecialCell(multiplier=2, multiplier_type=multiplier_type, icon=icon)
    
    def calculate_word_value(self, word, current_player):
        total_value = 0
        word_multiplier = 1

        # Calcular el valor total de la palabra y verificar los multiplicadores de palabra individual
        for cell in word:
            if isinstance(cell, Cell):
                letter_value = cell.calculate_value()
                total_value += letter_value

                if cell.multiplier_type == 'letter_word':
                    total_value *= cell.word_multiplier

                # Verificar si alguna celda tiene un multiplicador de palabra global
                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier

        total_value *= word_multiplier
        current_player.update_score(total_value)

        return total_value



    def change_state(self):
        ...
    

class Cell:
    def __init__(self, letter=None, multiplier=1, multiplier_type='', word_multiplier=1):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.word_multiplier = word_multiplier
        self.letter = letter

    def add_letter(self, letter: Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def is_multi(self):
        return self.multiplier_type in ['x2_letter', 'x3_letter', 'x2_word', 'x3_word']

    
class SpecialCell(Cell):
    def __init__(self, multiplier, icon, multiplier_type=''):
        super().__init__(multiplier=multiplier, multiplier_type=multiplier_type)
        self.icon = icon


