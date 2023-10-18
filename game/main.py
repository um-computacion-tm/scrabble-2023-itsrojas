from game.scrabble import ScrabbleGame, InvalidWordError

def main():
    print("Bienvenido!")
    players_count = 0
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")

    player_names = [] 

    for i in range(players_count):
        player_name = input(f"Ingrese el nombre del jugador {i + 1}: ")
        player_names.append(player_name)

    scrabble_game = ScrabbleGame(players_count=players_count, player_names=player_names)
    print("Cantidad de jugadores: ", len(scrabble_game.players))
    scrabble_game.next_turn()
    
    while True:
        if not scrabble_game.current_player.active:
            print(f"El jugador {scrabble_game.current_player.name} ha renunciado.")
            scrabble_game.next_turn()
            if ScrabbleGame.check_victory():
                break
            continue

        print(f"Turno del jugador {scrabble_game.current_player.id}, {scrabble_game.current_player.name} - Puntaje actual: {scrabble_game.current_player.score}")
        word = input("Ingrese palabra (o 'resign' para renunciar, 'skip' para saltar el turno): ").strip().upper()
        if word == 'SKIP':
            scrabble_game.skip_turn()
        elif word == 'RESIGN':
            scrabble_game.resign_player(scrabble_game.current_player_index)
            print(f"El jugador {scrabble_game.current_player.id} ha renunciado.")
            scrabble_game.next_turn()
        else:
            location_x = input("Ingrese posicion X: ")
            location_y = input("Ingrese posicion Y: ")
            location = (location_x, location_y)
            orientation = input("Ingrese orientacion (V/H)").strip().upper()
            try:
                scrabble_game.validate_word(word, location, orientation)
                # Lógica adicional para calcular puntajes y verificar si el juego termina
            except InvalidWordError as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    main()
    
#X
