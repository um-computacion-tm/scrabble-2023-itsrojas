import unittest

from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())


if __name__ == '__main__':
    unittest.main()