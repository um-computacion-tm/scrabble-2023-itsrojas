import unittest
from game.scrabble_board import Board, InvalidPlaceWordException
from game.scrabble_objects import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False


    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        assert board.is_empty == False

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = [Tile('F', 4), Tile('A', 1), Tile('C', 3), Tile('U', 1), Tile('L', 1), Tile('T', 1), Tile('A', 1), Tile('D', 2)]
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = [Tile('F', 4), Tile('A', 1), Tile('C', 3), Tile('U', 1), Tile('L', 1), Tile('T', 1), Tile('A', 1), Tile('D', 2)]
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = [Tile('F', 4), Tile('A', 1), Tile('C', 3), Tile('U', 1), Tile('L', 1), Tile('T', 1), Tile('A', 1), Tile('D', 2)]
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True 

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = [Tile('F', 4), Tile('A', 1), Tile('C', 3), Tile('U', 1), Tile('L', 1), Tile('T', 1), Tile('A', 1), Tile('D', 2)]
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_horizontal_valid(self):
        board = Board()
        word = "FACULTAD"
        location = (7, 4)
        orientation = "H"

        board.place_word(word, location, orientation)
        for index, letter in enumerate(word):
            cell = board.grid[7][4 + index]
            self.assertEqual(cell.letter.letter, letter)

    def test_place_word_vertical_valid(self):
        board = Board()
        word = "FACULTAD"
        location = (4, 7)
        orientation = "V"

        board.place_word(word, location, orientation)
        for index, letter in enumerate(word):
            cell = board.grid[4 + index][7]
            self.assertEqual(cell.letter.letter, letter)


    
            
    def test_list_words(self):
        board = Board()
        board.grid[7][4].add_letter(Tile('F', 4))
        board.grid[7][5].add_letter(Tile('A', 1))
        board.grid[7][6].add_letter(Tile('C', 3))
        board.grid[7][7].add_letter(Tile('U', 1))
        board.grid[7][8].add_letter(Tile('L', 1))
        board.grid[7][9].add_letter(Tile('T', 1))
        board.grid[7][10].add_letter(Tile('A', 1))
        board.grid[7][11].add_letter(Tile('D', 2))

        words = board.list_words()
        expected_words = ['FACULTAD']

        self.assertEqual(words, expected_words)

    def test_get_word_without_intersections_horizontal(self):
        board = Board()
        board.grid[7][4].add_letter(Tile('F', 4))
        board.grid[7][5].add_letter(Tile('A', 1))
        board.grid[7][6].add_letter(Tile('C', 3))
        board.grid[7][10].add_letter(Tile('A', 1))
        board.grid[7][11].add_letter(Tile('D', 2))

        word = "FACULTAD"
        location = (7, 4)
        orientation = "H"

        no_intersections = board.get_word_without_intersections(word, location, orientation)
        expected_result = 'ULT'

        self.assertEqual(no_intersections, expected_result)

    def test_get_word_without_intersections_vertical(self):
        board = Board()
        board.grid[4][7].add_letter(Tile('F', 4))
        board.grid[5][7].add_letter(Tile('A', 1))
        board.grid[6][7].add_letter(Tile('C', 3))
        board.grid[10][7].add_letter(Tile('A', 1))
        board.grid[11][7].add_letter(Tile('D', 2))

        word = "FACULTAD"
        location = (4, 7)
        orientation = "V"

        no_intersections = board.get_word_without_intersections(word, location, orientation)
        expected_result = 'ULT'

        self.assertEqual(no_intersections, expected_result)

    def test_show_board(self):
        board = Board()
        expected_board ="""       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ TW3 │     │     │ DL2 │     │     │     │ TW3 │     │     │     │ DL2 │     │     │ TW3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ DW2 │     │     │     │ TL3 │     │     │     │ TL3 │     │     │     │ DW2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ DW2 │     │     │     │ DL2 │     │ DL2 │     │     │     │ DW2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ DL2 │     │     │ DW2 │     │     │     │ DL2 │     │     │     │ DW2 │     │     │ DL2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ DW2 │     │     │     │     │     │ DW2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ TL3 │     │     │     │ TL3 │     │     │     │ TL3 │     │     │     │ TL3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │     │ DL2 │     │     │     │ DL2 │     │ DL2 │     │     │     │ DL2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │ TW3 │     │     │ DL2 │     │     │     │ DW2 │     │     │     │ DL2 │     │     │ TW3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │     │     │ DL2 │     │     │     │ DL2 │     │ DL2 │     │     │     │ DL2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │ TL3 │     │     │     │ TL3 │     │     │     │ TL3 │     │     │     │ TL3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │     │     │     │ DW2 │     │     │     │     │     │ DW2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │ DL2 │     │     │ DW2 │     │     │     │ DL2 │     │     │     │ DW2 │     │     │ DL2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │     │     │ DW2 │     │     │     │ DL2 │     │ DL2 │     │     │     │ DW2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │ DW2 │     │     │     │ TL3 │     │     │     │ TL3 │     │     │     │ DW2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │ TW3 │     │     │ DL2 │     │     │     │ TW3 │     │     │     │ DL2 │     │     │ TW3 │
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
        self.maxDiff = None
        self.assertEqual(expected_board, repr(board))


