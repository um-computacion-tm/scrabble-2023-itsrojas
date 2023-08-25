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
- changelog do not collect test data(status: unsolved)

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

