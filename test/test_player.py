import unittest
from game.scrabble_objects import BagTiles, Tile
from game.scrabble_player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.bag = BagTiles()

    def test_init(self):
        player_1 = Player(player_id=1)  
        self.assertEqual(len(player_1.hand), 0)

    def test_draw_initial_tiles(self):
        player = Player(bag_tiles=self.bag)
        player.draw_initial_tiles()
        self.assertEqual(len(player.hand), 7)

    def test_add_tiles(self):
        player = Player(bag_tiles=self.bag)
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        player.add_tiles(tiles)
        self.assertEqual(len(player.hand), 3)

    def test_remove_tiles(self):
        player = Player(bag_tiles=self.bag)
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        player.add_tiles(tiles)
        tiles_to_remove = [tiles[0], tiles[2]]
        player.remove_tiles(tiles_to_remove)
        for tile in tiles_to_remove:
            self.assertNotIn(tile, player.hand)
        self.assertEqual(len(player.hand), 1)

    def test_exchange_tiles(self):
        player = Player(bag_tiles=self.bag)
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]
        player.add_tiles(tiles)
        original_tiles = player.hand[:]
        tiles_to_exchange = [tiles[0], tiles[2]]
        player.exchange_tiles(tiles_to_exchange)
        self.assertEqual(len(player.hand), 4)
        self.assertNotEqual(player.hand, original_tiles)

    def test_update_score(self):
        player = Player(bag_tiles=self.bag)
        word_value = 10
        player.update_score(word_value)
        self.assertEqual(player.points, 10)

    def test_validate_user_has_letters(self):
        player = Player(bag_tiles=self.bag)
        player.hand = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        tiles = ['H', 'O', 'L', 'A']

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        player = Player(bag_tiles=self.bag)
        player.hand = [
            Tile(letter='P', value=3),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        tiles = ['H', 'O', 'L', 'A']

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, False)

    def test_rack_representation(self):
        player = Player(bag_tiles=self.bag)
        player.hand = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        expected_rack_repr = "Player(name='', points=0, rack=[H:4, O:1, L:1, A:1, C:3, U:1, M:3])"

        self.assertEqual(repr(player), expected_rack_repr)


if __name__ == '__main__':
    unittest.main()

