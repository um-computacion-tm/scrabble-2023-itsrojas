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

    def __repr__(self):
        spaces = " " * 4
        horizontal_line = spaces + "┌" + "─────┬" * 14 + "─────┐" + "\n"
        middle_horizontal_line = spaces + "├" + "─────┼" * 14 + "─────┤" + "\n"
        bottom_horizontal_line = spaces + "└" + "─────┴" * 14 + "─────┘"

        board = " " * 5 + " ".join([str(i).center(5, " ") for i in range(15)]) + "\n"
        board += horizontal_line

        for i in range(15):
            board += f"{str(i).rjust(3)} │"
            for j in range(15):
                cell = self.grid[i][j]
                if cell.letter is not None:
                    cell_repr = f"{cell.letter}".center(5, " ")
                elif cell.multiplier_type == 'DL':
                    cell_repr = f"DL{cell.multiplier}".center(5, " ")
                elif cell.multiplier_type == 'TL':
                    cell_repr = f"TL{cell.multiplier}".center(5, " ")
                elif cell.multiplier_type == 'DW':
                    cell_repr = f"DW{cell.multiplier}".center(5, " ")
                elif cell.multiplier_type == 'TW':
                    cell_repr = f"TW{cell.multiplier}".center(5, " ")
                else:
                    cell_repr = "     "
                board += cell_repr + "│"
            board += "\n"
            if i != 14:
                board += middle_horizontal_line
        board += bottom_horizontal_line
        return board
  

    def get_word_letters(self, word, location, orientation):
        word_cells = []
        row, col = location

        for index, letter in enumerate(word):
            if orientation.upper() == 'H':
                if 0 <= col + index < 15:
                    cell = self.grid[row][col + index]
                    word_cells.append(cell.letter.letter if cell.letter is not None else None)
                else:
                    word_cells.append(None)
            elif orientation.upper() == 'V':
                if 0 <= row + index < 15:
                    cell = self.grid[row + index][col]
                    word_cells.append(cell.letter.letter if cell.letter is not None else None)
                else:
                    word_cells.append(None)

        return word_cells
    
    def get_word_cells(self, word, location, orientation):
        row, col = location
        word_cells = []

        for letter in word:
            if 0 <= row < 15 and 0 <= col < 15:
                word_cells.append(self.grid[row][col])
            if orientation.upper() == 'H':
                col += 1
            elif orientation.upper() == 'V':
                row += 1

        return word_cells

    def list_words(self):
        words = []
        current_word = []

        for row in self.grid:
            for cell in row:
                if cell.letter is not None:
                    current_word.append(cell.letter.letter)
                else:
                    if current_word:  # Asegura que solo se agreguen palabras no vacías
                        words.append(''.join(current_word))
                    current_word = []

        if current_word:  # Agrega la última palabra si no está vacía
            words.append(''.join(current_word))

        # Agrega el siguiente código para devolver las palabras completas
        words = [word for word in words if len(word) > 1]

        return words
    
    def validate_crossing_words(self, word, location, orientation):
        if self.is_empty:
            return True

        row, col = location

        for i, letter in enumerate(word):
            cross_row, cross_col = (row, col + i) if orientation == 'H' else (row + i, col)

            if cross_row < 0 or cross_row >= 15 or cross_col < 0 or cross_col >= 15:
                continue  # La palabra se encuentra fuera del tablero, sigue verificando

            if self.grid[cross_row][cross_col].letter is not None:
                existing_tile = self.grid[cross_row][cross_col].letter
                if existing_tile.letter != letter:
                    return False
        return True

    def get_word_without_intersections(self, word, location, orientation):
        result = ''
        row, col = location

        for i in range(len(word)):
            if self.grid[row][col].letter is None:
                result += word[i]

            if orientation == 'H':
                col += 1
            elif orientation == 'V':
                row += 1

        return result
        
    def validate_word_inside_board(self, word, location, orientation):
        position_x, position_y = location
        len_word = len(word)

        if orientation == "H":
            return 0 <= position_x < 15 and 0 <= position_y < 15 and position_x + len_word <= 15
        elif orientation == "V":
            return 0 <= position_x < 15 and 0 <= position_y < 15 and position_y + len_word <= 15
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
                    self.current_cell.add_letter(Tile(letter, 1))  # Crear una instancia de Tile
                return True
        else:
            if orientation == "H":
                for i, letter in enumerate(word):
                    self.current_cell = self.grid[position_x][position_y + i]
                    if self.current_cell.letter is not None and self.current_cell.letter.letter != letter:
                        return False
                    else:
                        self.current_cell.add_letter(Tile(letter, 1))
                return True
            elif orientation == "V":
                for i, letter in enumerate(word):
                    self.current_cell = self.grid[position_x + i][position_y]
                    if self.current_cell.letter is not None and self.current_cell.letter.letter != letter:
                        return False
                    else:
                        self.current_cell.add_letter(Tile(letter, 1))
                return True
            else:
                return False

    def place_word(self, word, location, orientation):
        position_x, position_y = location
        if orientation == 'H':
            for index, letter in enumerate(word.upper()):
                self.current_cell = self.grid[position_x][position_y + index]
                self.current_cell.add_letter(Tile(letter, 1))  # Crear una instancia de Tile
        elif orientation == 'V':
            for index, letter in enumerate(word.upper()):
                self.current_cell = self.grid[position_x + index][position_y]
                self.current_cell.add_letter(Tile(letter, 1))  # Crear una instancia de Tile
        else:
            raise InvalidPlaceWordException('Orientación Invalida')
