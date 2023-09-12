import unittest

from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles


class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []

        for _ in range(players_count):
            self.players.append(Player(board=self.board, bag_tiles=self.bag_tiles))

        self.current_player_index = None

    def next_turn(self):
        if self.current_player_index is None:
            self.current_player_index = 0
        else:
            # Calcula el índice del siguiente jugador circularmente
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        self.current_player = self.players[self.current_player_index]




    
if __name__ == '__main__':
    unittest.main()