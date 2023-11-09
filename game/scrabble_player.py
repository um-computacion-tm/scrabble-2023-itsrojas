from game.scrabble_objects import BagTiles, Tile

class InvalidHandError(Exception):
    pass

class Player:
    def __init__(self, bag_tiles=None, points=0, name="", active=True, player_id=None): 
        if bag_tiles is None:
            bag_tiles = BagTiles()
        self.bag = bag_tiles
        self.hand = self.bag.take(0)
        self.name = name
        self.points = points
        self.active = active
        self.id = player_id 
        self.tile = Tile(letter='', value=0)
        self.skip_count = 0

    
    def get_name(self):
        return self.name
    
    def __repr__(self):
        return f"Player(name='{self.name}', points={self.points}, rack={self.hand})"


    def draw_initial_tiles(self, initial_letters=None):
        if initial_letters is None:
            initial_letters = self.bag.take(7)  # Cambiar 0 a 7
            self.hand.extend(initial_letters)
            return self.hand
        else:
            pass
        
    def refill_tiles(self):
        while len(self.hand) < 7:
            new_tiles = self.bag.take(7 - len(self.hand))
            self.hand.extend(new_tiles)
        return self.hand

    def add_tiles(self, tiles):
        self.hand.extend(tiles)
        return self.hand

    def remove_tiles(self, tiles_to_remove):
        for tile in tiles_to_remove:
            if tile in self.hand:
                self.hand.remove(tile)
        return self.hand

    def exchange_tiles(self, tiles_to_exchange):
        for tile in tiles_to_exchange:
            if tile in self.hand:
                self.hand.remove(tile)
        self.bag.put(tiles_to_exchange)
        new_tiles = self.bag.take(len(tiles_to_exchange))
        self.hand.extend(new_tiles)
        return self.hand

    def update_score(self, word_value):
        self.points += word_value

    def has_letters(self, word):
        player_letters = [self.tile.letter for self.tile in self.hand]
        player_letter_count = {letter: player_letters.count(letter) for letter in set(player_letters)}
        for letter in word:
            if letter not in player_letter_count or player_letter_count[letter] == 0:
                return False
            player_letter_count[letter] -= 1
        return True
