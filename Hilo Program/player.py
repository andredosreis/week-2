from card import Card
import random

class Player:
    """"
    """
    Score = None
    


    def __init__(self):
        """

        """

        self.is_playing = True
        self.score = 300
        self.total_score = 0
        self.cards = random.randint(1, 13)


    def start_game(self):
        while self.is_playing:
            self.roll_card()
            self.get_inputs()
            self.do_updates()


    def roll_card(self):
        """

        :return:
        """
        print('You will star with 300 score points')
        print(f'The card is: {self.cards}')

    def get_inputs(self):
        roll_hile = input('Higher or Lower?[h/l]')
        self.is_playing = (roll_hile == "h")
        if roll_hile
        self.cards







    def do_updates(self):
        """

       :return:
        """
 #       if not self.is_playing:
  #          return

   #     else:
    #        if self.get_inputs() < self.cards:
      #          print('Mais ... try again')
     #       elif self.get_inputs() > self.cards:
       #         print('low... try again')



