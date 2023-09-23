import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest
from unittest.mock import patch

from game.scrabble_objects import BagTiles, Tile
from game.scrabble_board import Board, Cell, SpecialCell
from game.scrabble_player import Player
from game.scrabble import ScrabbleGame, InvalidWordError


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        board = Board()
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertIsNotNone(scrabble_game.bag_tiles)
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[0])

    def test_next_turn_when_player_is_not_the_first(self):
        # Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player_index = 0  # Establece el jugador actual al jugador 0

        scrabble_game.next_turn()

        assert scrabble_game.current_player_index == 1

    def test_next_turn_when_player_is_last(self):
        # Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_word_inside_board(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()  # Asegúrate de establecer el jugador actual antes de dibujar las letras iniciales
        scrabble_game.current_player.draw_initial_tiles(scrabble_game.bag_tiles)

        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        # Verificar si se lanza la excepción InvalidWordError
        with self.assertRaises(InvalidWordError):
            scrabble_game.validate_word(word, location, orientation)

    def test_word_out_of_board(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()  # Asegúrate de establecer el jugador actual antes de dibujar las letras iniciales
        scrabble_game.current_player.draw_initial_tiles(scrabble_game.bag_tiles)

        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        # Verificar si se lanza la excepción InvalidWordError
        with self.assertRaises(InvalidWordError):
            scrabble_game.validate_word(word, location, orientation)


if __name__ == '__main__':
    unittest.main()