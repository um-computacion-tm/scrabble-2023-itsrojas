import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, repo_root)

import unittest
from game.main import main 
    
'''    @patch('builtins.print')
    @patch('game.cli.show_player')
    @patch('game.cli.show_board')
    @patch('game.cli.get_player_count', return_value=3)
    @patch('game.cli.get_inputs', return_value=((1, 3), 'H', 'CASA'))
    @patch.object(ScrabbleGame, 'is_playing', side_effect=[True, False])
    @patch.object(ScrabbleGame, 'get_current_player', return_value=(0, "Player",))
    @patch.object(ScrabbleGame, 'play')
    def test_main(self, *args):
        main() '''

if __name__ == '__main__':
    unittest.main()