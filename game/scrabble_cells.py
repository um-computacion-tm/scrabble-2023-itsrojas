from game.scrabble_objects import Tile

class Cell:
    def __init__(
        self,
        multiplier=1,
        multiplier_type='',
        letter=None,
        multiplier_active=True,
    ):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.multiplier_active = multiplier_active
        self.letter = letter
        self.used = False

    def deactivate_multiplier(self):
        self.multiplier_active = False

    def add_letter(self, letter):
        self.letter = letter
        return self
    
    def calculate_value(self):
        if self.letter is None or self.used == True:
            return 0
        if self.multiplier_type == 'letter':
            self.used = True
            return self.letter.value * self.multiplier
        else:
            self.used = True
            return self.letter.value

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '

    def get_multiplier(row, col):
        dl_coordinates = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
        tl_coordinates = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
        dw_coordinates = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
        tw_coordinates = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

        if (row, col) in dl_coordinates:
            return 2  # Double Letter
        elif (row, col) in tl_coordinates:
            return 3  # Triple Letter
        elif (row, col) in dw_coordinates:
            return 4  # Double Word
        elif (row, col) in tw_coordinates:
            return 6  # Triple Word
        else:
            return 1

    def get_multiplier_type(row, col):
        dl_coordinates = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
        tl_coordinates = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
        dw_coordinates = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
        tw_coordinates = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

        if (row, col) in dl_coordinates:
            return "DL"
        elif (row, col) in tl_coordinates:
            return "TL"
        elif (row, col) in dw_coordinates:
            return "DW"
        elif (row, col) in tw_coordinates:
            return "TW"
        else:
            return ""  # No multiplier
        
    ''' def is_multi(self):
        return self.multiplier_type in {'x2_letter', 'x3_letter', 'x2_word', 'x3_word'}


    class SpecialCell(Cell):
        def __init__(self, multiplier, multiplier_type, icon):
            super().__init__(multiplier, multiplier_type)
            self.icon = icon '''
            
#X
