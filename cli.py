from game.scrabble import ScrabbleGame
from main import main

class Client:
    def __init__(self, player_count):
        self.scrabble_game = ScrabbleGame(player_count)
    
    def menu(self):
        print("------------------------------------Bienvenido a Scrabble-------------------------------------")
        print("Opciones de juego:")
        print("1. Mostrar tablero")
        print("2. Mostrar puntuaciones")
        print("3. Jugar palabra")
        print("4. Pasar turno")
        print("5. Intercambiar fichas")
        print("6. Salir del juego")
    
    def get_menu_option(self):
        try:
            option = int(input("Selecciona una opción: "))
            return option
        except ValueError:
            print("Opción no válida. Por favor, ingresa un número válido.")
            return self.get_menu_option()
    
    def get_player_count(self):
        player_count = int(input("Ingresa la cantidad de jugadores (entre 1 y 4): "))
        if player_count < 2 or player_count > 4:
            print("La cantidad de jugadores debe estar entre 2 y 4. Inténtalo de nuevo.")
            return self.get_player_count()
        return player_count
    
    def get_player_names(self, player_count):
        player_names = []
        for i in range(player_count):
            name = input(f"Ingresa el nombre del jugador {i + 1}: ")
            player_names.append(name)
        return player_names
    
    def display_game_info(self):
        print("Mostrando información del juego:")
        self.show_board()
        self.show_scores()
        self.show_tiles()
    
    def draw_tiles(self):
        self.scrabble_game.start_game()
    
    def player_turn(self):
        self.scrabble_game.play_turn()
    
    def show_tiles(self):
        player = self.scrabble_game.get_current_player()
        print(f"Fichas de {player.get_name()}: {player.get_tiles()}")
    
    def show_scores(self):
        scores = self.scrabble_game.get_scores()
        for player, score in scores.items():
            print(f"{player}: {score} puntos")
    
    def show_board(self):
        self.scrabble_game.get_board().show_board()
    
    def skip_turn(self):
        self.scrabble_game.skip_turn()
    
    def play_word(self):
        word = input("Ingresa la palabra a jugar: ")
        location = input("Ingresa la ubicación (fila, columna): ").split(',')
        orientation = input("Ingresa la orientación (H o V): ")
        self.scrabble_game.play(word, (int(location[0]), int(location[1])), orientation)
    
    def exchange_tiles(self):
        tiles_to_exchange = input("Ingresa las fichas a intercambiar (separadas por espacios): ").split()
        self.scrabble_game.exchange_tiles(tiles_to_exchange)
    
    def end_current_turn(self):
        self.scrabble_game.end_turn()
    
    def change_joker_to_tile(self):
        self.scrabble_game.change_joker_to_tile()
    
    def end_of_game(self):
        self.scrabble_game.end_game()
    
    def play_game(self):
        print("¡Bienvenido a Scrabble!")
        player_count = self.get_player_count()
        player_names = self.get_player_names(player_count)
        self.scrabble_game = ScrabbleGame(player_count, player_names)
        self.draw_tiles()

        while not self.end_of_game():
            self.display_game_info()
            self.menu()
            option = self.get_menu_option()

            if option == 1:
                self.show_board()
            elif option == 2:
                self.show_scores()
            elif option == 3:
                self.play_word()
            elif option == 4:
                self.skip_turn()
            elif option == 5:
                self.exchange_tiles()
            elif option == 6:
                print("¡Gracias por jugar Scrabble en línea de comandos. Hasta la próxima!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

    def graph_info(self):
        print("Gráficos de información del juego:")
        self.display_game_info()
                
if __name__ == '__main__':
    cli = Client(player_count=0)
    cli.play_game()
