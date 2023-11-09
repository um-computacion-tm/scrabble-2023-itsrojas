import unittest
from unittest.mock import patch

from game.scrabble_board import Board
from game.scrabble_player import Player
from game.scrabble_objects import BagTiles
from game.dictionary import dictionary_word
from game.scrabble import ScrabbleGame, InvalidWordError, InvalidPlayersCountException, InvalidWordException, InvalidPlaceWordException

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.next_turn()

        self.assertEqual(scrabble_game.current_player, 1)

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0

        scrabble_game.next_turn()

        self.assertEqual(scrabble_game.current_player, 1)

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 2

        scrabble_game.next_turn()

        self.assertEqual(scrabble_game.current_player, 0)

    def test_resign_player(self):
        game = ScrabbleGame(players_count=3)

        # Resign player 0
        game.resign_player(0)

        # Verify that player 0 is not active
        self.assertFalse(game.players[0].active)

        # Verify that players 1 and 2 are still active
        self.assertTrue(game.players[1].active)
        self.assertTrue(game.players[2].active)

        # Try to resign player 10
        with self.assertRaises(IndexError):
            game.resign_player(10)

    def test_game_over_empty_bag(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = []  # Vaciar la bolsa para simular su vaciamiento

        self.assertTrue(scrabble_game.empty_bag())
        self.assertTrue(scrabble_game.end_game())

    def test_validate_word_valid_word(self):
        game = ScrabbleGame(players_count=2)
        word = "HOLA"
        location = (7, 7)
        orientation = "H"
        self.assertTrue(game.validate_word(word, location, orientation))

    def test_validate_word_invalid_word(self):
        game = ScrabbleGame(players_count=2)
        word = "XZY"
        location = (7, 7)
        orientation = "H"
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)

    
    


if __name__ == '__main__':
    unittest.main()
