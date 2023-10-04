import unittest

from pyrae import dle
from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles

class InvalidWordError(Exception):
    pass


class ScrabbleGame:
    SEVEN_TILES_BONUS = 50
    def __init__(self, players_count: int, player_names: list):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []

        for i in range(players_count):
            self.players.append(Player(name=player_names[i], board=self.board, bag_tiles=self.bag_tiles))

        self.current_player_index = None
        self.current_player = None
        self.current_word = None
        self.current_turn = 0


    def next_turn(self):
        if self.current_player_index is None:
            self.current_player_index = 0
        else:
            # Calcula el índice del siguiente jugador circularmente
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        self.current_player = self.players[self.current_player_index]
        Player.refill_tiles

    def skip_turn(self):
        self.next_turn()

    def check_victory(self):
        active_players = [player for player in self.players if player.active]

        if len(active_players) == 1:
            winner = active_players[0]
            print(f"¡{winner.name} ha ganado el juego con {winner.points} puntos!")
            return True

        return False
        
    def validate_word(self, word, location, orientation):
        player = self.current_player
        if not player.has_letters(word.lower()):
            raise InvalidWordError("El jugador no tiene las letras necesarias para formar la palabra.")

        if not self.is_word_placement_valid(word, location, orientation):
            raise InvalidWordError("La palabra no cabe en el tablero o la orientación es incorrecta.")

        self.get_words(word, location, orientation)
        player.remove_letters(word)
        if len(word) == 7:
            player.update_score(self.SEVEN_TILES_BONUS)

    def is_word_placement_valid(self, word, location, orientation):
        row, col = location
        if orientation == "H":
            return col + len(word) <= 15
        elif orientation == "V":
            return row + len(word) <= 15
        return False

    def get_words(self, word, location, orientation):
        while True:
            res = dle.search_by_word(word=word)

            if res:
                print("Definición:", res.to_dict()['articles'][0]['definitions'][0]['sentence']['text'])
                is_real = input("¿Es esta palabra real? (S/N): ").strip().lower()

            # Llama a word_is_real para determinar si la palabra es real
                if self.word_is_real(is_real, word, location, orientation):
                    return  # Sal del bucle si la palabra es real
            else:
                print("Palabra no encontrada en el diccionario.")

    def word_is_real(self, is_real, word, location, orientation):
        if is_real == "s":
            self.current_player.board.place_word(word, location, orientation)
            return True  # Devuelve True si la palabra es real y se coloca en el tablero
        else:
            print("Palabra no válida.")
            return False  
        
    def resign_player(self, player_index):
        if 0 <= player_index < len(self.players):
            self.players[player_index].active = False


    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''
  
if __name__ == '__main__':
    unittest.main()