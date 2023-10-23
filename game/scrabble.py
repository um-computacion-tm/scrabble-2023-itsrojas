from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles
from game.dictionary import dictionary_word

class InvalidWordError(Exception):
    pass

class InvalidPlayersCountException(Exception):
    pass

class InvalidWordException(Exception):
    pass

class InvalidPlaceWordException(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = [Player(id=index, bag_tiles=self.bag_tiles) for index in range(players_count)]
        self.current_player = 0

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.board.calculate_word_value(words)
        self.players[self.current_player].update_score(total)
        self.next_turn()

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def skip_turn(self):
        self.next_turn()

    @staticmethod
    def get_player_count():
        while True:
            try:
                player_count = int(input('Cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except ValueError:
                print('Por favor, ingrese un número válido.')
        return player_count

    def resign_player(self, player_index):
        if 0 <= player_index < len(self.players):
            self.players[player_index].active = False
    
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

    def check_victory(self):
        active_players = [player for player in self.players if player.active]
        if len(active_players) <= 1:
            if active_players:
                winner = active_players[0]
                print(f"¡El jugador {winner.id}, {winner.name}, ha ganado la partida!")
            else:
                print("La partida ha terminado en empate.")
            return True
        return False

    def validate_word(self, word, location, orientation):
        if not dictionary_word(word):
            raise InvalidWordException("La palabra no existe en el diccionario.")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("La palabra excede el tablero.")
        if not self.board.validate_word_place_word(word, location, orientation):
            raise InvalidPlaceWordException("La palabra está mal ubicada en el tablero.")


        



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

        if len(word) == 7:
            player.update_score(SEVEN_TILES_BONUS) '''
       
#X
