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

        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
        # Obtiene el índice actual del jugador
            current_index = self.players.index(self.current_player)
        # Calcula el índice del siguiente jugador
            next_index = (current_index + 1) % len(self.players)
            self.current_player = self.players[next_index]



    
if __name__ == '__main__':
    unittest.main()