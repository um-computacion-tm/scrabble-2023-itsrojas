from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles
from game.dictionary import dictionary_word

class InvalidWordError(Exception):
    pass
class InvalidPlayersCountException(Exception):
    pass
class InvalidWordException(Exception):
    def __init__(self, message="La palabra no existe en el diccionario"):
        self.message = message
        super().__init__(self.message)

class InvalidPlaceWordException(Exception):
    def __init__(self, message="La palabra excede el tablero o está mal colocada"):
        self.message = message
        super().__init__(self.message)


class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(players_count):
            self.players.append(Player(id=index, bag_tiles=self.bag_tiles))
        
        self.current_player = None

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.board.calculate_words_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    
    def skip_turn(self):
        self.next_turn()
    
    def resign_player(self, player_index):
        if 0 <= player_index < len(self.players):
            self.players[player_index].active = False

    def check_victory(self):
        num_players = len(self.players)
        num_inactive_players = sum(1 for player in self.players if not player.active)

        if num_inactive_players >= num_players - 1:
            # Si queda solo un jugador activo o todos son inactivos, se ha completado la partida.
            active_players = [player for player in self.players if player.active]
            if active_players:
                active_player = active_players[0]
                print(f"¡El jugador {active_player.id}, {active_player.name}, ha ganado la partida!")
            else:
                print("La partida ha terminado en empate.")
            return True

        return False

    def validate_word(self, word, location, orientation):
        if not dictionary_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
            player.remove_letters(word)

    
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
    
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''

        



''' def _validate_players_count(self, players_count: int):
        if players_count < 2 or players_count > 4:
            raise InvalidPlayersCountException("El número de jugadores debe estar entre 2 y 4")

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()


    def check_victory(self):
        active_players = [player for player in self.players if player.active]

        if len(active_players) == 1:
            winner = active_players[0]
            print(f"¡{winner.name} ha ganado el juego con {winner.points} puntos!")
            return True

        return False
        
    def validate_word(self, word, location, orientation):
        player = self.players[self.current_player]

        if not player.has_letters(word.lower()):
            raise InvalidWordError("El jugador no tiene las letras necesarias para formar la palabra.")

        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidWordError("La palabra no cabe en el tablero o la orientación es incorrecta.")

        if not dictionary_word(word):
            raise InvalidWordError("La palabra no existe en el diccionario.")
        player.remove_letters(word)

         '''

''' def get_words(self, word, location, orientation):
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
            return False ''' 
