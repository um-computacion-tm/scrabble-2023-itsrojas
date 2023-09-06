import unittest

import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

from game.scrabble_objects import BagTiles, Tile
from game.scrabble_player import Player
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
    
    def setUp(self):
        self.player = Player() 
        self.bag = BagTiles() 

    def test_draw_initial_tiles(self):
        with patch.object(BagTiles, 'take') as mock_take:
            mock_take.return_value = [
                Tile('A', 1), Tile('B', 3), Tile('C', 3),
                Tile('D', 2), Tile('E', 1), Tile('F', 4), Tile('G', 2)
            ]
            player = Player()
            bag = BagTiles()
            player.draw_initial_tiles(bag)
            self.assertEqual(len(player.tiles), 7)

    def test_add_tiles(self):
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        self.player.add_tiles(tiles)
        self.assertEqual(len(self.player.tiles), 3)
        
    def test_remove_tiles(self):
        tile_A = Tile('A', 1)
        tile_B = Tile('B', 3)
        tile_C = Tile('C', 3)
        tiles = [tile_A, tile_B, tile_C]
        
        self.player.add_tiles(tiles)
        
        tiles_to_remove = [tile_A, tile_C]
        self.player.remove_tiles(tiles_to_remove)
        self.assertEqual(len(self.player.tiles), 1)
        self.assertEqual(self.player.tiles[0].letter, 'B')

    def test_exchange_tiles(self):
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]
        self.player.add_tiles(tiles)
        original_tiles = self.player.tiles[:]
        
        tiles_to_exchange = [Tile('A', 1), Tile('C', 3)]
        self.player.exchange_tiles(tiles_to_exchange, self.bag)
        
        self.assertEqual(len(self.player.tiles), 2)
        self.assertNotEqual(self.player.tiles, original_tiles)

if __name__ == '__main__':
    unittest.main()