from game.scrabble_objects import Tile

class Cell:
    def __init__(
        self,
        multiplier=1,
        multiplier_type='',
        letter=Tile(letter='',value=0),
        multiplier_active=True,
    ):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.multiplier_active = multiplier_active
        self.letter = letter
        self.used = False

    def add_letter(self, letter):
        if isinstance(letter, Tile):  
            self.letter = letter
        return self
    
    def deactivate_multiplier(self):
        if self.letter is not None and self.multiplier > 1:
            self.multiplier_active = False
        else:
            pass

    def calculate_value(self):
        if self.letter is None or self.used == True:
            return 0
        if self.multiplier_type == 'letter':
            self.used = True
            return self.letter.value * self.multiplier
        else:
            self.used = True
            return self.letter.value

    @classmethod
    def get_multiplier(cls, row, col):
        dl_coordinates = [(3, 0), (11, 0),(0, 3), (0, 11), (6, 2), (8, 2), (7, 3),(2, 6), (6, 6), (8, 6), (12, 6), (3, 7), (11, 7), (2, 8), (6, 8), (8, 8), (12, 8), (8, 12), (7, 11), (6, 12), (8, 12), (14, 3), (14, 11),
                          (3, 14), (11, 14)] 
        tl_coordinates = [(5, 1), (9, 1), (1, 5), (5, 5), (9, 5), (13, 5), (1, 9), (5, 9), (9, 9), (13, 9), (5, 13), (9, 13)]
        dw_coordinates = [(1, 1), (13, 1), (2, 2), (12, 2), (3, 3), (11, 3), (4, 4), (10, 4), (7, 7), (4, 10), (10, 10), (3, 11), (11, 11), (2, 12), (12, 12), (1, 13), (13, 13)]
        tw_coordinates = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

        if (row, col) in dl_coordinates:
            return 2  # Double Letter
        elif (row, col) in tl_coordinates:
            return 3  # Triple Letter
        elif (row, col) in dw_coordinates:
            return 2  # Double Word
        elif (row, col) in tw_coordinates:
            return 3  # Triple Word
        else:
            return 1
    @classmethod
    def get_multiplier_type(cls, row, col):
        dl_coordinates = [(3, 0), (11, 0),(0, 3), (0, 11), (6, 2), (8, 2), (7, 3),(2, 6), (6, 6), (8, 6), (12, 6), (3, 7), (11, 7), (2, 8), (6, 8), (8, 8), (12, 8), (8, 12), (7, 11), (6, 12), (8, 12), (14, 3), (14, 11),
                          (3, 14), (11, 14)] 
        tl_coordinates = [(5, 1), (9, 1), (1, 5), (5, 5), (9, 5), (13, 5), (1, 9), (5, 9), (9, 9), (13, 9), (5, 13), (9, 13)]
        dw_coordinates = [(1, 1), (13, 1), (2, 2), (12, 2), (3, 3), (11, 3), (4, 4), (10, 4), (7, 7), (4, 10), (10, 10), (3, 11), (11, 11), (2, 12), (12, 12), (1, 13), (13, 13)]
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
            return ""  
