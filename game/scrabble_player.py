from game.scrabble_objects import Tile, BagTiles

class InvalidHandError(Exception):
    pass

class Player:
    def __init__(self, bag_tiles=None, points=0, name=""):
        if bag_tiles is None:
            bag_tiles = BagTiles()
        self.bag = bag_tiles
        self.tiles = self.bag.take(0)
        self.object = Tile('', 0)  
        self.name = name
        self.points = points
        self.hand = []
        self.active = True

    def draw_initial_tiles(self, initial_letters=None):
        if initial_letters is None:
            initial_letters = self.bag.take(7)
            self.hand.extend(initial_letters)
            return self.hand
        else:
            pass

    def refill_tiles(self):
        while len(self.hand) < 7:
            new_tiles = self.bag.take(7 - len(self.hand))
            self.hand.extend(new_tiles)
        return self.hand

    def add_tiles(self, tiles):
        self.hand.extend(tiles)
        return self.hand

    def remove_tiles(self, tiles_to_remove):
        for tile in tiles_to_remove:
            if tile in self.hand:
                self.hand.remove(tile)
        return self.hand

    def exchange_tiles(self, tiles_to_exchange):
        for tile in tiles_to_exchange:
            if tile in self.hand:
                self.hand.remove(tile)
        self.bag.put(tiles_to_exchange)
        new_tiles = self.bag.take(len(tiles_to_exchange))
        self.hand.extend(new_tiles)
        return self.hand

    def update_score(self, word_value):
        self.points += word_value

    def has_letters(self, tiles):
        tile_dict = {}
        for self.tile in self.hand:
            if self.object.letter not in tile_dict:
                tile_dict[self.object.letter] = 1
            else:
                tile_dict[self.object.letter] += 1

        for self.tile in tiles:
            if self.object.letter not in tile_dict or tile_dict[self.object.letter] == 0:
                if '?' in tile_dict and tile_dict['?'] > 0:
                    tile_dict['?'] -= 1
                else:
                    return False
            else:
                tile_dict[self.object.letter] -= 1
        return True


    """Verifica si el jugador tiene todas las letras necesarias para formar la palabra.

    Args:
        tiles: Una lista de objetos Tile que representan las letras de la palabra.

    Returns:
        True si el jugador tiene todas las letras necesarias, False en caso contrario.
    """

#X



