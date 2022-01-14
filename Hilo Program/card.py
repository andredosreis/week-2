import random

class Card:
    """

    """
    #play is score
    score = None
    #Is the player still playing
    is_playing = None
    # Is the player's guess high?
    guess_is_high = None
    # The player's name.
    name = ""



    def __init__(self, name, starting_score):
        self.is_playing = True
        self.name = name
        self.score = starting_score

    def roll(self):

        self.value = random.randint(1, 13)
