from game.play import CardPlay

class Director:

    def __init__(self):
        
        self.card = CardPlay()
        self.is_playing = True
        self.score = 300
        self.decision = ""

    def start_game(self):

        self.deal_card()
        while self.is_playing:
            print (f'\nThe card is: {self.card.deal1}')
            self.play()            
            self.continue_game()
            self.message()

    def deal_card(self):
        self.card.deal()

    def play(self):
        self.card.score_computing()
        print (f'\nThe card was {self.card.deal2}')
        print (f'Your score is {self.card.score}')

    def continue_game (self):
        self.decision = input ('\nPlay again? [y/n] ')
        self.is_playing = (self.decision == "y" and self.card.score > 0)
        self.card.deal1 = self.card.deal2

    def message(self):
        if self.card.score <= 0 or self.decision != "y":
            print ('\nGame Over!!')
