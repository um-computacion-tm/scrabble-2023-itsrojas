import unittest
from game.scrabble_objects import Tile, BagTiles
from game.scrabble_board import Board

class Player:
    def __init__(self,board=None, bag_tiles=None, points=0):
        self.tiles = []
        self.points = points
        self.bag_tiles = bag_tiles 
        self.board = board

    def draw_initial_tiles(self, bag):
        initial_tiles = bag.take(7)
        self.add_tiles(initial_tiles)

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

    def has_letters(self, word):
        letter_count = {}
        for tile in self.tiles:
            if tile.is_wildcard:
                letter_count['?'] = letter_count.get('?', 0) + 1
            else:
                letter = tile.letter
                letter_count[letter] = letter_count.get(letter, 0) + 1
        for letter in word:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            letter_count[letter] -= 1

        return True




