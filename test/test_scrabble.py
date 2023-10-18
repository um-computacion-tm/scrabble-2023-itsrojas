import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest
from unittest.mock import patch

from pyrae import dle
from game.scrabble_objects import BagTiles
from game.scrabble_board import Board
from game.scrabble import ScrabbleGame, InvalidWordError


''' class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        board = Board()
        player_names = ["Jugador1", "Jugador2", "Jugador3"]
        scrabble_game = ScrabbleGame(players_count=3, player_names=player_names)
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

    def setUp(self):
        # Mueve la creación de la instancia de ScrabbleGame a la función setUp
        player_names = ["Jugador1", "Jugador2"]
        self.game = ScrabbleGame(players_count=2)
        self.game.next_turn()
        self.game.current_player.draw_initial_tiles(self.game.bag_tiles)
        self.game.current_player.board = self.game.board


    def test_next_turn_when_game_is_starting(self):
        player_names = ["Jugador1", "Jugador2", "Jugador3"]
        scrabble_game = ScrabbleGame(players_count=3, player_names=player_names)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, "Jugador1")

    def test_next_turn_when_player_is_not_the_first(self):
        # Validar que luego del jugador 0, le toca al jugador 1
        player_names = ["Jugador1", "Jugador2", "Jugador3"]
        scrabble_game = ScrabbleGame(players_count=3, player_names=player_names)
        scrabble_game.current_player_index = 0  # Establece el jugador actual al jugador 0

        scrabble_game.next_turn()

        assert scrabble_game.current_player_index == 1

    def test_next_turn_when_player_is_last(self):
        player_names = ["Jugador1", "Jugador2", "Jugador3"]
        scrabble_game = ScrabbleGame(players_count=3, player_names=player_names)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, "Jugador1")

    def test_word_inside_board(self):
        player_names = ["Jugador1", "Jugador2", "Jugador3"]
        scrabble_game = ScrabbleGame(players_count=3, player_names=player_names)
        scrabble_game.next_turn()  # Asegúrate de establecer el jugador actual antes de dibujar las letras iniciales
        scrabble_game.current_player.draw_initial_tiles(scrabble_game.bag_tiles)

        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        # Verificar si se lanza la excepción InvalidWordError
        with self.assertRaises(InvalidWordError):
            scrabble_game.validate_word(word, location, orientation)

    def test_word_out_of_board(self):
        player_names = ["Jugador1", "Jugador2", "Jugador3"]
        scrabble_game = ScrabbleGame(players_count=3, player_names=player_names)
        scrabble_game.next_turn()  # Asegúrate de establecer el jugador actual antes de dibujar las letras iniciales
        scrabble_game.current_player.draw_initial_tiles(scrabble_game.bag_tiles)

        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        # Verificar si se lanza la excepción InvalidWordError
        with self.assertRaises(InvalidWordError):
            scrabble_game.validate_word(word, location, orientation)

    
    def test_place_word_and_change_state(self):
        player_names = ["Jugador1", "Jugador2"]
        scrabble_game = ScrabbleGame(players_count=2, player_names=player_names)
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
        player_names = ["Jugador1", "Jugador2"]
        scrabble_game = ScrabbleGame(players_count=2, player_names=player_names)
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
        player_names = ["Jugador1", "Jugador2"]
        scrabble_game = ScrabbleGame(players_count=2, player_names=player_names)
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
        game = ScrabbleGame(players_count=players_count, player_names=["Jugador1", "Jugador2", "Jugador3"])

        # Jugador 1 renuncia
        game.resign_player(0)
        self.assertFalse(game.players[0].active)  # Verifica que el jugador 1 esté inactivo

        # Jugador 2 sigue activo
        self.assertTrue(game.players[1].active)

        # Jugador 3 sigue activo
        self.assertTrue(game.players[2].active)

        # Prueba con un índice fuera de rango
        game.resign_player(10)

    def test_seven_tiles_bonus(self):
        player_names = ["Jugador1", "Jugador2"]
        scrabble_game = ScrabbleGame(players_count=2, player_names=player_names)
        scrabble_game.next_turn()

        # Jugar exactamente siete fichas en un turno
        word = "PALABRA"
        location = (7, 7)
        orientation = "H"

        # Asegúrate de que el jugador tenga las fichas necesarias antes de jugar
        scrabble_game.current_player.tiles = ["P", "A", "L", "A", "B", "R", "A"]

        # Coloca la palabra en el tablero
        scrabble_game.validate_word(word, location, orientation)

        # Verifica que el jugador haya recibido el bono de 50 puntos
        self.assertEqual(scrabble_game.current_player.points, ScrabbleGame.SEVEN_TILES_BONUS)

    def test_refill_tiles(self):
        # Verifica que al final del turno se rellenan las fichas del jugador
        player = self.game.current_player
        initial_tile_count = len(player.tiles)

        # Llama a la función para rellenar las fichas
        self.game.next_turn()  # Llama a next_turn para avanzar al siguiente turno

        # Verifica que el jugador tenga 7 fichas al final del turno
        self.assertEqual(len(player.tiles), 7)

    def test_check_victory_single_winner(self):
        # Creamos un juego de Scrabble con tres jugadores
        scrabble_game = ScrabbleGame(players_count=3)
        
        # Simulamos la victoria de un jugador
        scrabble_game.players[0].active = True
        scrabble_game.players[1].active = False
        scrabble_game.players[2].active = False

        # Verificamos si se declara al jugador activo como ganador
        self.assertTrue(scrabble_game.check_victory()) '''



if __name__ == '__main__':
    unittest.main()
    
#X

