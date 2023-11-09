import unittest
from game.scrabble_objects import BagTiles, Tile
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


if __name__ == '__main__':
    unittest.main()
