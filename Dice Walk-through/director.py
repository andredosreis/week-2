
class  Director:

    def __init__(self):
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)



    def start_game(self):
        """
        Runs the game loop.
        :arg self(Director): an instance od Director
        :return:
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    def get_inputs(self):
        """
        ask teh user if they wat to roll.
        :arg self(Director): An istance of Director.
        :return:
        """
        roll_dice = input('Roll dice?[y/n]')
        self.is_playing = (roll_dice == "y")

    def do_updates(self):
        """
        rolls the dice.
        :arg self(Diretor): an instance of Director
        :return:
        """
        if not self.is_playing:
            return

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points
            self.total_score += self.score

    def do_outputs(self):
        """
        Display the results.

        :arg self(Director): An instance of Director
        :return:
        """

        if not self.is_playing:
            return

        values = ""

        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value}"

            print(f"you rolled {values}")
            print(f'your score is {self.total_score}')
            self.is_playing == (self.score > 0)

        



