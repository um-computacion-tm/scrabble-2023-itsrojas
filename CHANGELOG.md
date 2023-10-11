# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- repository creation
- 'scrabble_objects.py' creation
- 'scrabble_tests.py' creation
- coverage installation
## [1.0.0] - 2023-08-20

### Added
- tiles added
- wildcard tiles added
- 'Bagtiles' added
- 'take' function implemented
- 'put' function implemented
- coveragearc creation
### Fixed
- fixed docker key error

## [1.0.1] -2023-08-21

### Added
- Updated wildcard capability to `Tile` class
- Updated `BagTiles` class to include wildcard tiles and all the other letters
- Added 'TestWildcards' on  'scrabble_tests.py' to verify if wildcards works
- Updated 'TestTiles' to verify wildcard functioning
- Updated 'game' directory with 'gamescrabble'

### Known Issues
- coverage do not collect test data(status: unsolved)

## [1.0.2] -2023-08-22

### Fixed
- Fixed changelog and coverage data collection issues
- fixed github directory mess

### Changed
- changed 'scrabblegame' directory into 'game'
- changed 'scrabble_test' into 'test_scrabble'
### Dropped
- Dropped old directory Trabajo_scrabble

## [1.0.3] -2023-08-24

### Added
- 'scrabble' creation
- 'scrabble_player' creation
- 'scrabble_board' creation
- added new tests to 'test_scrabble'
- added new branch to github

### Changed
- changed circleci connection
- changed .gitignore instructions
- changed .coverage instructions

## [1.0.4] -2023-08-27

### Added
- Added 'SpecialCell' class, derived of the 'Cell' class of scrabble_board, to implement special cells
- Added 'is_multi' method to 'Cell' to determine the special cells.
- Added 'define_special_cells' to 'Board' to configure the special cell of the board.
- Added a new test to verify if the special cells works.

### Changed
- Changed '__init__' method of Board so it can call define_special_cells during the method.
- Changed '__init__' method of Player so the player begins with a puntuation of 0

### Fixed
- Fixed 'TestBagtiles' from 'test_scrabble' so it can now have the real number of tiles that the bagtile has.
- Fixed 'player' class points so it bagins with 0 paints and it doesn`t crash the test

## [1.0.5] -2023-08-28

### Added
- Added 'add_tiles' in 'scrabble_player.py' that allows to add some tiles to the player's hand. 
- Added 'remove_tiles' in 'scrabble_player.py'that allows to remove specific tiles tiles from the player's hand.
- Added 'exchange_tiles' in 'scrabble_player.py' facilitate tile exchange with the tile bag.
- Added new tests to 'test_scrabble,py' to verify new functions.

### Fixed
- Fixed the import in 'scrabble_player.py'so it can finally works
- Reconnected circleCi with the repository.

## [1.0.6] -2023-08-29

### Added
- Added 'draw_initial_tiles' to 'scrabble_player.py' so each player can begin wit their initial tiles
- Added new test on 'test_scrabble.py' so it can be seen if the initial tiles code works

### Changed
- Optimized the code
- fixed some changelog grammar errors.

### Dropped
- Removed requirements.txt from github

### Known error
- Circleci webpage don`t allow to sign up leading instead to this link: https://circleci.com/hooks/github?signup-404=true (unsolved)

## [1.0.7] -2023-08-30

### Added
- Added 'test_player.py' to the archives to separate and optimize the tests.
- Added 'test_board.py' to the archives to separate and optimize the tests.
- Added 'test_objects.py' to the archives to seprate the tests.
- Added new test  to 'test_board.py'

### Changed
- Reduced the code in 'test_scrabble.py' and make it specific for the tests for scrabble.py


## [1.0.8] -2023-09-5

### Added
- Added new connection to Code Climate to github and circleci.
- Added the tests of 'test_board.py' to 'test_scrabble.py' to analyse an error.

### Fixed

- Fixed errors on some tests that dind`t recognized the ubication of the repository

### Dropped

- Dropped 'test_board.py'

### Known Error

- There is still an error in 'test_scrabble.py' that doesn't seem to recognize some objects of some archives but the proggram still recognizes them. I think that the main problem is relaate to 'scrabble_board.py'

## [1.0.9] -2023-09-6 

## Added
- Added again 'test_board.py' after solving the recognition error.
- Added new function to 'ScrabbleGame' 'next_turn' to advance turns in the game.
- Added a new test to verify the new function.

## Changed
- changed the '__init__' function of 'scrabble_player.py' so it can now have bag_tiles
- changed the '__init__' function of 'scrabble.py' so it can work with the points.
- changed import that 'scrabble_board.py' has so it can work correctly with 'scrabble_objects.py'

## Fixed
- Finally fixed the circleCI and code climate connection by purgin all of the java datas of the repositry
- Fixed the recognition error of the test by changing the import of 'scrabble_board.py' to 'game.scrabble_objects'
- Fixed the config.yml of circleCI so it can now work properly.
## Dropped
- Dropped some trash files of the repository

## [1.1.0] -2023-09-7 

## Added
- Added a new function `calculate_word_value` to `scrabble_board.py` that calculates the value of a word formed on the game board. 
- Added a new test to see if the function works.

## [1.1.1] -2023-09-8

## Added
- Added the attribute 'word_multiplier' to 'cell' and 'board' class so they can now track and use the words multipliers correctly.
- Added new test to 'test_boarb.py' so it can verify if the code uses the differents multipliers well. 

## Changed
- Changed the way on how the 'calculate_word_value' method works by adding a way that it can multiply the word multipliers now and so it doesn`t mess up the order of the operation
- Adjusted the 'calculate_value' method in the 'Cell' class to use the individual word multiplier if the multiplier type is 'letter_word' in the new code.

## [1.1.2] -2023-09-10

## Added
- Added new method to 'scrabble_player.py' being that 'update_score' so the players could keep up with their points during the game
- Added new test to verify the new method

## Changed
- Optimized the codes of 'scrabble.py' and 'scrabble_board.py' so it could work better and pass the coverage test better
- Optimized the test with the same reason and to fixes some problems with the new code

## Dropped
- Dropped reccursive method from 'SpecialCell' because its functions were already repeated on other merthod from the code.

## [1.1.3] -2023-09-12

## Added
- Added new tests to 'test_board.py' and 'test_scrabble.py' so it can test the new functions of the code
## Changed
- Changed the code of the 'next_turn' method of 'scrabble.py' so that player`s turns are rotated circularly.
- Changed the code of the 'calculate_word_value' method of 'scrabble_board.py' so it gain the capacity to deactivate the special cells and their multipliers so the code doesn`t repeat already used multipliers

## [1.1.4] -2023-09-20

## Added
- Added the code of 'main.py' into the 'game' directory to configure the game
- Added but not completed the methods of 'validate_word', 'get_words' and 'put_words' on 'scrabble.py' to complete later

## [1.1.5] -2023-09-22

## Added
- Added 'has_letter' method to 'Player' class to verify if the player has the necesary letters for the word
- Added new tests to 'test_player.py' to verify if 'has_letter' works

## Notes
- with 'has_letter' set and working i can now has the code and process necesary to make the method of 'validate_word' work into the code


## [1.1.6] -2023-09-23

## Added
- Added the exception `InvalidWordError` into 'scrabble.py' to handle the error related to invalid words
- Added the code of 'validate_word' to 'scrabble.py'to validate if a word is valid to put on the board
- Added `place_word` method to `Scrabble.py` to place the word on the board if it is valid.
- Added new tests to verify the new addition

## Changed
-Updated some codes in `scrabble.py` to adapt to the new functionality.
-Updated the `ScrabbleGame` constructor of 'scrabble.py' to initialize `current_player` and `current_player_index`.

## [1.1.7] -2023-09-24

## Added
- Added the 'change_state' method to 'scrabble_board.py' so it could alter the state of the cells on the board
- Added an 'is_occupied' attribute to 'cell' so it can show whn the cell has a letter or not
- Added new test to verify the new functions.

## Changed
- updated and changed places of the method 'place_word' to 'scrabble_board.py' so it works better
- updated the method 'place_word' on 'scrabble.py' so it can now use the new code implemented

## [1.1.8] -2023-09-25

## Added
- Added the method of 'get_word' to 'scrabble.py' so it can recognize the if the word that the player puts exists
- Imported the program of pyrae to serve as the dictionary for the words

## Known problems
- There is a problem with the pyrae in that the tests doesn`t recognize the pyrae and it doesn`t allow it to function. I am going to have to search later

## Notes
- I have been focusing most on solving the pyrae problem, so maybe that part of the code doesn`t work in this version and the 'get_word' is not fully operational for now, so i am going to fix it later. And it may be need an overhoul of that method.
- So 'get_word' can`t be considered an success yet.

## [1.1.9] -2023-09-26

## Added
-Added method 'skip_turn' to 'scrabble.py' so if the player decides or has no other option, they could skip their turn.

## Changed
- Finished coding the 'get_word' method of 'scrabble.py' so it can now fully recognize words and it works
- Modified the codes of 'validate_word', 'get_word' and 'place_word' so they con now work together

## Fixed
- Fixed the problem with pyrae where the app doesn`t work nd now it works perfectly

## Notes
- 'skip_turn' it`s incomplete for now and it will be worked later, so for now. It doesn`t have tests and it isn`t called by any objects or method.

## [1.2.0] -2023-09-27

## Added
- Added pyrae into 'requirements.txt' to work with circleCi,because i forgot to add it last commit.
- Added the methods of 'get_letters_count', 'is_word_placement_valid' and 'calculate_word_multiplier' to 'scrabble.py' , 'scrabble_player.py' and 'scrabble_board.py' so the code can be simplified

## Changed
- Changed some of the code of 'scrabble.py' , 'scrabble_player.py' and 'scrabble_board.py' so the code can be simplified and it could pass code climate.

##Notes
- The code of 'main.py' said its a little complex to code climate, but the code is the same from the code of slack and i haven`t complete worked with the code and the level of complexity is very little. So i will work on it latter.

## [1.2.1] -2023-10-01

## Added
- Added new method to 'scrabble.py' that is 'resign_player' so that a player can abbandon the game without causing problems to the other players.
- Added an 'active' attribute to the Player class to keep track if the player is in the game or abandoned it

## Changed
- Modified the 'main.py' code so that it can works with the pass and resing code

## [1.2.2] -2023-10-02

## Added
- Added atribute 'SEVEN_TILES_BONUS' in 'scrabble.py' to give a 50 points bonus for the player that uses 7 tiles in on word according to the rules of the game
- Added in 'scrabble_player.py', a name parameter to  specify the player's name when creating a play
- 'main.py' now allows entering player names at the start of the game, instead of automatically assigning numeric identifiers.
- Added a new test to verify the changes.

## Changes
- Changed the ScrabbleGame constructor from 'scrabble.py' to now use the specified names
- Updated the 'validate_word' method to verify if the player used the 7 tiles and if its correct , it now grants the 15 points bonus.
- Changed the printing of the active player's name in 'word_is_real' to reflect the name of the player.
- CHanged some parts of the code of 'scrabble.py' to not cause many problems with the bonus points and the names

## [1.2.2] -2023-10-03

## Added
- Added 'check_victory' method to 'scrabble.py' so it can give a victory to the plaer if they are the only left, it`s still incomplete.
- Added the 'refill_tiles' method on 'scrabble_player.py' so at the end of each turn all the player get 7 tiles in total
- Added new test to verify the new implementations

## Changed
- Modified the codes of 'scrabble.py', 'scrabble_player.py' and 'main.py' to work with the new code

## Notes
-check victory is incomplete for now and refill_tiles is going to be adapted to the player module si it may not work for now

## [1.2.3] -2023-11-08

## Added:

# scrabble.py:

- Added the import of dictionary_word from dictionary.py to check if a word exists in the dictionary.
- Added a new method _validate_players_count to validate the number of players.
- Introduced a dictionary word validation feature in the validate_word method.
- Added resign_player method to set a player as inactive.
# scrabble_player.py:

- Added the refill_tiles method to refill a player's tiles after placing a word.
# scrabble_board.py:
- Added get_multiplier method to calculate cell multipliers.
- Added validate_word_inside_board method to check word placement validity.
# scrabble_cells.py:
- Added cells.py with their respective methods and attributes
# main.py:

- Updated to check for game victory after each turn.
# dictionary.py:

- Added dictionary.py

## Changed:

# scrabble.py:
- Removed player_names from the constructor and simplified player creation.
- Updated game logic to handle turns and word placement more efficiently.
- Moved the SEVEN_TILES_BONUS constant outside of the class as a global constant.
# scrabble_board.py:

- Updated define_special_cells to use a dictionary for special cell locations.
## Moved:

# scrabble.py:
- Moved the SEVEN_TILES_BONUS constant outside of the class as a global constant.

## Dropped:

# scrabble.py:
- Dropped unnecessary code for calculating the current player's index in the next_turn method.
- Removed the put_words method, as it is not implemented.

## Known errors
- due to mayor overhaul of the code, many test are going to be rewritten to fit the code but i dind`t have time to finish and fixing them so they would be fixed tomorrow

## Note
- I am sorry proffesor for the mess

## [1.2.4] -2023-11-09

## Added:

- Added a calculate_value method to the Tile class in scrabble_objects.py to calculate the value of a tile.
- Added 'is_empty' property to 'scrabble_board.py' so it can detect the game when the board and the cells are empty
- Added the 'get_multiplier' and 'get_multiplier_type' methods in the Cell class so that in this method the special cells could be identified and not in board
- Added the '__repr__' method in 'scrabble_cells.py' and 'scrabble_objects.py' to start with the graphic representation

## Changed:

- Updated the Board class in scrabble_board.py to use the new Tile class when filling the board.
- Replaced the calculate_value method in the Cell class in scrabble_cells.py with a calculate_value method that considers the tile's value and multiplier.
- Modified the codes of 'place_word' and 'validate_word' and moved them to 'scrabble_board', and have them work the two directly on board

## Dropped:
- Removed the way of getting the multiplier cells in scrabble_board.py so it could be accesed directly from the cell class
- 'specialcell' class is going to be removed if it is an easer way to directly use the Cell class

## Notes:

- Since now many parts of the code will begin to have ''' ''' and that means that that code is "quarantine" that means that i put the code in a halt until id decided to put them back in the code  beacuse it gives error or because it is usseles code for now, those codes are in risk to be dropped.
- Sorry proffesor for the last two commits and changelogs because for the past week i have been trying to merge both my code with the code of the proffesors in one big commit, but i messed it up completely with my code and it is now a chaos. I am searching for some way to download a previous commit code so i can fix my mistake.
- But for now i have been remaking and optimizing my code so i can fix this problem i have put myself in, so these new commits will be of more fixing my mistake of the last commit so i am sorry if many of the code now has broken or if i don`t add very significal thinks for my mistake.
- So for now i am going to try to fix my fault and try to make my code more similar to the proffesor codes, once again. I am sorry for these last commits.

## [1.2.5] -2023-11-10

## Added:

- Added new test for the use of main and dictionary
- Added new exceptions to scrabble.py so 'validate_words' works within the profesor`s code

## Changed:

- Changed and fixed 'calculate_word_value' so it can work with the new code and it would fit with the proffesors code
- Fixed 'validate_word_insided_word' and 'validate_word_place_word' so it can work with the new init of board and could work well
- Completed and fixed 'check_victory' on scrabble.py so it can finally work within the rules of srabble
- Modified 'players_count' code
- some of the porblematic and old code is put into cuarantine until new advice.

## Fixed:

- fixed on of the biggest problem i had within the big commit three commits ago and is that i implemented self.tiles on cell when it isn`t used. Now i changed that into self.letter that i used and many of the problems with the code were fixed.
- Fixed many of the problems with i had within the old tests and with calculate_word.

## Notes:
- Begin the work to fix scrabble.py

