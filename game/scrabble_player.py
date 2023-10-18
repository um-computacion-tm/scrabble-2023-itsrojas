from game.scrabble_objects import Tile, BagTiles
from game.scrabble_board import Board

class Player:
    def __init__(self,board=None, bag_tiles=None, points=0, name=""):
        self.tiles = []
        self.name = name
        self.points = points
        self.bag_tiles = bag_tiles 
        self.board = board
        self.active = True

    def draw_initial_tiles(self, bag, initial_letters=None):
        if initial_letters is None:
            initial_letters = bag.take(7)
        self.add_tiles(initial_letters)

    def refill_tiles(self):
        while len(self.tiles) < 7:
            new_tiles = self.bag_tiles.take(7 - len(self.tiles))
            self.add_tiles(new_tiles)

    def add_tiles(self, tiles):
        self.tiles.extend(tiles)

    def remove_tiles(self, tiles):
        self.tiles = [tile for tile in self.tiles if tile not in tiles]

    def exchange_tiles(self, tiles_to_exchange, bag):
        new_tiles = bag.take(len(tiles_to_exchange))
        bag.put(tiles_to_exchange)
        bag.put(self.tiles)
        self.tiles = new_tiles

    def update_score(self, word_value):
        self.points += word_value

    def get_letter_count(self):
        letter_count = {}
        for tile in self.tiles:
            if isinstance(tile, Tile):  # Verifica si el objeto es una instancia de la clase Tile
                if tile.is_wildcard:
                    letter_count['?'] = letter_count.get('?', 0) + 1
                else:
                    letter = tile.letter
                    letter_count[letter] = letter_count.get(letter, 0) + 1
        return letter_count
    
    def has_letters(self, tiles):
        letter_count = {}
        for tile in self.tiles:
            if isinstance(tile, Tile):  # Verifica si el objeto es una instancia de la clase Tile
                if tile.is_wildcard:
                    letter_count['?'] = letter_count.get('?', 0) + 1
                else:
                    letter = tile.letter
                    letter_count[letter] = letter_count.get(letter, 0) + 1

        for tile in tiles:
            letter = tile.letter
            if letter not in letter_count or letter_count[letter] == 0:
                return False

        return True

    """Verifica si el jugador tiene todas las letras necesarias para formar la palabra.

    Args:
        tiles: Una lista de objetos Tile que representan las letras de la palabra.

    Returns:
        True si el jugador tiene todas las letras necesarias, False en caso contrario.
    """

#X



