import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

from game.scrabble_objects import BagTiles, Tile
from game.scrabble_board import Board, Cell, SpecialCell
from game.scrabble_player import Player
from game.scrabble import ScrabbleGame



import unittest
from unittest.mock import patch


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)



if __name__ == '__main__':
    unittest.main()