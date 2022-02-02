import random

class CardPlay:
    def __init__(self):

        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.deal1 = 0
        self.deal2 = 0
        self.score = 300

    def deal(self):          
        self.deal1 = int (random.choice(self.cards))

    def score_computing(self):
        self.deal2 = int (random.choice(self.cards))
        guess = input ('Higher or Lower? [h/l] ')
        if guess == "h":
            if self.deal2 >= self.deal1:
                self.score += 100
            else:
                self.score -= 75
        else:
            if self.deal2 >= self.deal1:
                self.score -= 75
            else:
                self.score += 100        
        