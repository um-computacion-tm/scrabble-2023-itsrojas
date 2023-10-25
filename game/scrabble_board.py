from game.scrabble_cells import Cell  
from game.scrabble_objects import Tile  


class InvalidPlaceWordException(Exception):
    pass

class Board:
    def __init__(self, fill_with=" " * (15*15)):
        self.grid = [
            [
                Cell(
                    letter=Tile(fill_with[(row * 15) + col], 1) if fill_with[(row * 15) + col] != " " else None,
                    multiplier=Cell.get_multiplier(row, col),
                    multiplier_type=Cell.get_multiplier_type(row, col),
                )
                for col in range(15)
            ]
            for row in range(15)
        ]
        self.current_cell = Cell()

    @property
    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.letter is not None:
                    return False
        return True

    @staticmethod
    def calculate_word_value(word):
        value = 0
        multiplier_word = 1  
        
        for cell in word:
            value += cell.calculate_value()
            if cell.multiplier_type == "word" and cell.multiplier_active:
                multiplier_word = cell.multiplier
                cell.deactivate_multiplier()
        if len(word) == 7:
            value += 50
        return value * multiplier_word 

    def show_board(self):  
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.grid): 
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )

    def validate_word_inside_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)

        if orientation == "H":
            if position_x + len_word > 15 or position_x < 0 or position_y < 0:
                return False
            return True
        elif orientation == "V":
            if position_y + len_word > 15 or position_x < 0 or position_y < 0:
                return False
            return True
        else:
            return False
        
    def validate_word_place_word(self, word, location, orientation):
        if not self.validate_word_inside_board(word, location, orientation):
            return False

        position_x = location[0]
        position_y = location[1]

        if self.is_empty:
            if orientation == "H" and location[0] != 7:
                return False
            elif orientation == "V" and location[1] != 7:
                return False
            else:
                for i, letter in enumerate(word):
                    if orientation == "H":
                        self.current_cell = self.grid[position_x][position_y + i]
                    elif orientation == "V":
                        self.current_cell = self.grid[position_x + i][position_y]
                    self.current_cell.add_letter(Tile(letter, 1))
                return True
        else:
            if orientation == "H":
                for i, letter in enumerate(word):
                    current_cell = self.grid[position_x][position_y + i]
                    if self.current_cell.letter is not None and self.current_cell.letter != letter:
                        return False
                    else:
                        self.current_cell.add_letter(Tile(letter, 1))
                        return True
            elif orientation == "V":
                for i, letter in enumerate(word):
                    current_cell = self.grid[position_x + i][position_y]
                    if self.current_cell.letter is not None and self.current_cell.letter != letter:
                        return False
                    else:
                        self.current_cell.add_letter(Tile(letter, 1))
                        return True
            else:
                return False
            



    """ Places a word on the board.

    Args:
        word: A list of letters.
        location: A tuple of coordinates (row, col).
        orientation: A string, either "H" or "V".

    Raises:
        InvalidPlaceWordException: If the word cannot be placed on the board.
        """
        
    '''@staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        word_value: int = 0
        letter_multipliers = []  # Almacenar multiplicadores de letra
        word_multiplier = 1

        for cell in word:
            letter_value = cell.calculate_value()
            if cell.multiplier_type == "letter":
                letter_multipliers.append(cell.multiplier)
            word_value += letter_value

        # Aplicar multiplicadores de letra
        for multiplier in letter_multipliers:
            word_value *= multiplier

        # Aplicar multiplicadores de palabra
        for cell in word:
            if cell.multiplier_type == "word":
                word_multiplier *= cell.multiplier

        # Aplicar multiplicadores de palabra y sumar puntos por letras
        word_value *= word_multiplier

        # Aplicar premio por "scrabble" (7 letras utilizadas)
        if len(word) == 7:
            word_value += 50

        return word_value'''
    


    def change_state(self, row, col, letter=None, score=0):
        self.current_cell = self.grid[row][col]
        self.current_cell.letter = letter
        self.current_cell.score = score
        self.current_cell.is_occupied = True


#X
