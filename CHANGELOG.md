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


