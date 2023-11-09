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
    def __init__(self, players_count: int, player_names=None):
        self.board = Board()
        self.bag_tiles = BagTiles()
        if player_names is None:  
            player_names = [f"Player {i}" for i in range(players_count)]
        self.players = [Player(player_id=index, bag_tiles=self.bag_tiles, name=player_names[index]) for index in range(players_count)]
        self.current_player = 0

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        word_cells = self.board.extend_word(word, location, orientation)  # Extiende la palabra en el tablero
        words = [cell.letter.letter for cell in word_cells]
        total = self.board.calculate_word_value(words)
        self.players[self.current_player].update_score(total)
        self.next_turn()

    def get_active_players_count(self):
        active_players_count = sum(player.active for player in self.players)
        return active_players_count
        
    def _validate_players_count(self, players_count: int):
        if players_count < 2 or players_count > 4:
            raise InvalidPlayersCountException("El número de jugadores debe estar entre 2 y 4")
        

    def start_game(self):
        for player in self.players:
            player.draw_initial_tiles()
            player.refill_tiles()
        self.board.show_board()

    def get_scores(self):
        scores = {}
        for player in self.players:
            scores[player.get_name()] = player.points
        return scores 

    def next_turn(self):
        if self.end_game():
            return

        self.current_player = (self.current_player + 1) % len(self.players)

    def skip_turn(self):
        if self.end_game():
            return

        self.next_turn()

    def resign_player(self, player_index):
        if 0 <= player_index < len(self.players):
            self.players[player_index].active = False
        else:
            raise IndexError("Player index out of range")

    def _validate_players_count(self, players_count: int):
        if players_count < 2 or players_count > 4:
            raise InvalidPlayersCountException("El número de jugadores debe estar entre 2 y 4")

    def validate_word(self, word, location, orientation):
        if not dictionary_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_word(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra está mal puesta en el tablero")

        # Obtener las celdas de la palabra válida
        word_cells = self.board.get_word_cells(word, location, orientation)
        return word_cells
        
    def end_game(self):
        if self.empty_bag():
            self.display_final_scores()
            return True

        if self.board_full():
            self.display_final_scores()
            return True

        if self.players_decide_to_end_game():
            self.display_final_scores()
            return True
        
        return False

    def display_final_scores(self):
        scores = self.get_scores()  # Obtener los puntajes internamente
        final_scores = []
        for player_name, score in scores.items():
            final_scores.append(f"{player_name}: {score} points")
        return final_scores

    def empty_bag(self):
        return len(self.bag_tiles.tiles) == 0
    
    def players_decide_to_end_game(self):
        active_players = [player for player in self.players if player.active]
        return not active_players
    
    def board_full(self):
        if self.empty_bag():
            return all(len(player.hand) == 0 for player in self.players if player.active)
        return False
        
    def put_words(self, word, location, orientation):
        word_cells = self.validate_word(word, location, orientation)
        total = self.board.calculate_word_value(word_cells)
        self.players[self.current_player].update_score(total)
        self.board.place_word(word, location, orientation)
        self.next_turn()        
