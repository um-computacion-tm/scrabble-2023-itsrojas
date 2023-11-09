from game.scrabble import ScrabbleGame
from cli import Client

def main():
    cli = Client(player_count=0)
    cli.start_game()


if __name__ == '__main__':
    main()

