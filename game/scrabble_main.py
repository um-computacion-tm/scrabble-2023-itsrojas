import unittest
from game.scrabble_board import Board
from game.scrabble_objects import BagTiles
from game.scrabble_player import Player

class ScrabbleMain:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))
        
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            #index = index del current player + 1
            #len(self.players)
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def validate_word(self, word, location, orientation):
        ...
        ## validar que un usuario tenga esas letras
        ## validar que las palabra entre en el tablero
        ## validar que la palabra exisa
        ...
        self.board. 

    def put_word(self, word, location, orientation):
        ...
        # modifica el estado del tablero con las palabras consideradas como correctas