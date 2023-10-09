from game.scrabble_objects import Tile

class Cell:
    def __init__(self, letter=None, value=1, multiplier=1, multiplier_type='', word_multiplier=1):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.word_multiplier = word_multiplier
        self.letter = letter
        self.is_occupied = False 

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '

    def add_letter(self, letter: Tile):
        self.letter = letter
        self.is_occupied = True 

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def is_multi(self):
        return self.multiplier_type in {'x2_letter', 'x3_letter', 'x2_word', 'x3_word'}

class SpecialCell(Cell):
    def __init__(self, multiplier, multiplier_type, icon):
        super().__init__(multiplier, multiplier_type)
        self.icon = icon