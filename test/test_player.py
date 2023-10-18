import unittest

import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

from game.scrabble_objects import BagTiles, Tile
from game.scrabble_player import Player
from unittest.mock import patch
from game.scrabble_board import Board

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(bag_tiles=BagTiles())
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def setUp(self):
        self.bag = BagTiles()  # Mueve la creación de self.bag aquí
        self.player = Player(board=None, bag_tiles=self.bag, points=0)  # Luego crea self.player
        # Agregar exactamente 7 fichas iniciales
        initial_tiles = [
            Tile('A', 1), Tile('B', 3), Tile('C', 3),
            Tile('D', 2), Tile('E', 1), Tile('F', 4), Tile('G', 2)
        ][:7]
        self.player.add_tiles(initial_tiles)

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
        self.assertEqual(len(self.player.tiles), 10)  # Debería haber 10 fichas en total
        
    def test_remove_tiles(self):
        tile_A = Tile('A', 1)
        tile_B = Tile('B', 3)
        tile_C = Tile('C', 3)
        tiles = [tile_A, tile_B, tile_C]
    
        self.player.add_tiles(tiles)
    
        tiles_to_remove = [tile_A, tile_C]
        self.player.remove_tiles(tiles_to_remove)
    
        for tile in tiles_to_remove:
            self.assertNotIn(tile, self.player.tiles)
    
        self.assertEqual(len(self.player.tiles), 8)

    def test_exchange_tiles(self):
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]
        self.player.add_tiles(tiles)
        original_tiles = self.player.tiles[:]
        
        tiles_to_exchange = [Tile('A', 1), Tile('C', 3)]
        self.player.exchange_tiles(tiles_to_exchange, self.bag)
        
        self.assertEqual(len(self.player.tiles), 2)
        self.assertNotEqual(self.player.tiles, original_tiles)

    def test_update_score(self):
        # Crear un jugador y un tablero
        bag = BagTiles()
        board = Board()
        player = Player(board=board, bag_tiles=bag, points=0)

        # Definir un valor de palabra y actualizar el puntaje del jugador
        word_value = 10
        player.update_score(word_value)

        # Comprobar que el puntaje del jugador se ha actualizado correctamente
        self.assertEqual(player.points, 10)

    '''def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)

        self.assertTrue(is_valid)

    # Verifica que las fichas se hayan consumido correctamente
        letter_count = player.get_letter_count()
        for tile in tiles:
            letter = tile.letter
            self.assertTrue(letter_count.get(letter, 0) > 0)
            letter_count[letter] -= 1 '''

    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=3),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=4
                 ),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, False)

    

if __name__ == '__main__':
    unittest.main()
    
#X
