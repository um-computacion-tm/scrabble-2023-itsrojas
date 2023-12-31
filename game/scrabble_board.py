from game.scrabble_cells import Cell  
from game.scrabble_objects import Tile  

class Board:
    def __init__(self, fill_with=" " * (15*15)):
        self.grid = [
            [
                Cell(
                    letter=(
                        Tile(
                            letter=fill_with[(row * 15)+col], value=1
                        ) 
                        if fill_with[(row * 15)+col] != " " 
                        else None
                    ),
                    multiplier=Cell.get_multiplier(row, col),
                    multiplier_type=Cell.get_multiplier_type(row, col),
                )
                for col in range(15)
            ]
            for row in range(15)
        ]

    @property
    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.letter is not None:
                    return False
        return True

    @staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.multiplier_active:
                multiplier_word = cell.multiplier
                cell.deactivate_multiplier()  
        if multiplier_word:
            value = value * multiplier_word
        if len(word) == 7:
            value += 50
        return value

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
                        current_cell = self.grid[position_x][position_y + i]
                    elif orientation == "V":
                        current_cell = self.grid[position_x + i][position_y]
                    current_cell.add_letter(Tile(letter, 1))
                return True
        else:
            if orientation == "H":
                for i, letter in enumerate(word):
                    current_cell = self.grid[position_x][position_y + i]
                    if current_cell.letter is not None and current_cell.letter.letter != letter:
                        return False
                    current_cell.add_letter(Tile(letter, 1))
                return True
            elif orientation == "V":
                for i, letter in enumerate(word):
                    current_cell = self.grid[position_x + i][position_y]
                    if current_cell.letter is not None and current_cell.letter.letter != letter:
                        return False
                    current_cell.add_letter(Tile(letter, 1))
                return True
            else:
                return False
            
    def place_word(self, word, location, orientation):
        position_x, position_y = location
        for letter in word:
            if orientation == "H":
                current_cell = self.grid[position_x][position_y]
                position_y += 1
            elif orientation == "V":
                current_cell = self.grid[position_x][position_y]
                position_x += 1
            else:
                return False
            current_cell.add_letter(Tile(letter, 1))



        
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


''' def change_state(self, row, col, letter=None, score=0):
        cell = self.grid[row][col]
        cell.letter = letter
        cell.score = score
        cell.is_occupied = True '''

''' def calculate_word(self, word):
        total_value = 0
        word_multiplier = 1

        # Calcular el valor total de la palabra y verificar los multiplicadores de palabra individual
        for cell in word:
            letter_value = cell.calculate_value()
            if cell.multiplier_type == 'letter_word' and cell not in self.used_special_cells:
                letter_value *= cell.word_multiplier
            total_value += letter_value

        # Verificar si alguna celda tiene un multiplicador de palabra global
        for cell in word:
            if cell.multiplier_type == 'word' and cell not in self.used_special_cells:
                word_multiplier *= cell.multiplier
        word_multiplier = self.calculate_word_multiplier(word)

        total_value *= word_multiplier

        return total_value


    def calculate_word_multiplier(self, word):
        word_multiplier = 1
        for cell in word:
            if cell.multiplier_type == 'word' and cell not in self.used_special_cells:
                word_multiplier *= cell.multiplier
        return word_multiplier '''

