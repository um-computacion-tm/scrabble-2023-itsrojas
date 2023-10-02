import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest
from unittest.mock import patch

from pyrae import dle
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

    
    def test_place_word_and_change_state(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.draw_initial_tiles(scrabble_game.bag_tiles)

        word = "HELLO"
        location = (7, 7)
        orientation = "H"

        # Crea una instancia de la clase Board
        scrabble_board = scrabble_game.board

        # Coloca la palabra en el tablero y cambia el estado de las celdas
        scrabble_board.place_word(word, location, orientation)

        # Verifica que el estado de las celdas haya cambiado a "ocupado"
        for i, letter in enumerate(word):
            cell = scrabble_board.grid[location[0]][location[1] + i]
            self.assertEqual(cell.letter, letter)
            self.assertTrue(cell.is_occupied)  # Verifica que la celda esté ocupada

    @patch('builtins.input', return_value='S')
    def test_get_word_valid_word(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.next_turn()
        word = "HOLA"
        location = (7, 7)
        orientation = "H"
        scrabble_game.current_player.board.place_word(word, location, orientation)

        # Assumimos que get_word se llama dentro de validate_word, por lo que probamos validate_word
        with self.assertRaises(InvalidWordError):
            scrabble_game.validate_word(word, location, orientation)

    @patch('builtins.input', return_value='N')
    def test_get_word_invalid_word(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.next_turn()
        word = "XYZ"
        location = (7, 7)
        orientation = "H"

        # Assumimos que get_word se llama dentro de validate_word, por lo que probamos validate_word
        with self.assertRaises(InvalidWordError):
            scrabble_game.validate_word(word, location, orientation)

    def test_put_words(self):
        pass  # Reemplazar luego

    def test_resign_player(self):
        bag = BagTiles()
        board = Board()
        players_count = 3  # Cambia la cantidad de jugadores según tu necesidad
        game = ScrabbleGame(players_count=players_count)

        # Jugador 1 renuncia
        game.resign_player(0)
        self.assertFalse(game.players[0].active)  # Verifica que el jugador 1 esté inactivo

        # Jugador 2 sigue activo
        self.assertTrue(game.players[1].active)

        # Jugador 3 sigue activo
        self.assertTrue(game.players[2].active)

        # Prueba con un índice fuera de rango
        game.resign_player(10)


if __name__ == '__main__':
    unittest.main()
