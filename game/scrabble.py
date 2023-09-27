import unittest

from pyrae import dle
from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles

class InvalidWordError(Exception):
    pass


class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []

        for _ in range(players_count):
            self.players.append(Player(board=self.board, bag_tiles=self.bag_tiles))

        self.current_player_index = None
        self.current_player = None

    def next_turn(self):
        if self.current_player_index is None:
            self.current_player_index = 0
        else:
            # Calcula el índice del siguiente jugador circularmente
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        self.current_player = self.players[self.current_player_index]
    
    def validate_word(self, word, location, orientation):
        # 1. Validar que el usuario tiene las letras necesarias
        player = self.current_player
        if not player.has_letters(word):
            raise InvalidWordError("El jugador no tiene las letras necesarias para formar la palabra.")

        # 2. Validar que la palabra entra en el tablero
        row, col = location
        if orientation == "H":
            end_col = col + len(word)
            if end_col > 15:
                raise InvalidWordError("La palabra no cabe en el tablero horizontalmente.")
        elif orientation == "V":
            end_row = row + len(word)
            if end_row > 15:
                raise InvalidWordError("La palabra no cabe en el tablero verticalmente.")
        else:
            raise InvalidWordError("La orientación debe ser 'H' (horizontal) o 'V' (vertical).")

        # Si todas las validaciones pasan, coloca la palabra en el tablero y actualiza las letras del jugador.
        self.board.place_word(word, location, orientation)
        player.remove_letters(word)
    
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
        while True:
            word = input("Ingrese una palabra: ")
            res = dle.search_by_word(word=word)

            if res:
            # Si se encuentra una definición, muestra la definición al usuario
                print("Definición:", res.to_dict()['articles'][0]['definitions'][0]['sentence']['text'])
                is_real = input("¿Es esta palabra real? (S/N): ").strip().lower()

                if is_real == "s":
                # Si el usuario la considera real, puedes continuar con esta palabra
                # Agrega aquí la lógica para continuar con la palabra en tu juego
                    pass
                else:
                    print("Palabra no válida.")
            else:
                print("Palabra no encontrada en el diccionario.")
    
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''
    # Hay que continuar arreglando la conexion con pyrae.

  
if __name__ == '__main__':
    unittest.main()