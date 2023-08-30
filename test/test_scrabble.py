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


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
        self.assertFalse(tile.is_wildcard)

    
class TestWildcards(unittest.TestCase):
    def test_wildcard_tile(self):
        tile = Tile('?', 0)
        tile.wildcard_tile('X', 8)
        self.assertEqual(tile.letter, 'X')
        self.assertEqual(tile.value, 8)
        self.assertTrue(tile.is_wildcard)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 10), Tile('Y', 4)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            102,
        )

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    
    def test_special_cells(self):
        board = Board()
        special_cells_positions = [
            (0, 0), (0, 7), (0, 14),
            (7, 0), (7, 14),
            (14, 0), (14, 7), (14, 14),
            (1, 5), (1, 9), (5, 1),
            (5, 5), (5, 9), (5, 13),
            (9, 1), (9, 5), (9, 9), (9, 13),
            (13, 5), (13, 9),
            (1, 1), (2, 2), (3, 3), (4, 4),
            (4, 10), (3, 11), (2, 12), (1, 13),
            (13, 1), (12, 2), (11, 3), (10, 4),
            (10, 10), (11, 11), (12, 12), (13, 13),
            (0, 3), (0, 12), (2, 6), (2, 8),
            (3, 0), (3, 7), (3, 14), (6, 2),
            (6, 6), (6, 8), (6, 12), (7, 3),
            (7, 11), (8, 2), (8, 6), (8, 8),
            (8, 12), (11, 0), (11, 7), (11, 14),
            (12, 6), (12, 8), (14, 3), (14, 11)
        ]
        
        for row in range(15):
            for col in range(15):
                if (row, col) in special_cells_positions:
                    self.assertIsInstance(board.grid[row][col], SpecialCell)
                else:
                    self.assertIsInstance(board.grid[row][col], Cell)

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )

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