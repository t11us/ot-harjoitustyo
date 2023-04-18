from traingenerator import TrainGenerator
from drawdeck import DrawDeck

class TrainDeck:
    def __init__(self, traingenerator):
        self.tgen = traingenerator

        #initialize deck
        self.deck = []
        for i in range(0,self.tgen.colornum):
            self.deck.append(0)
            
        
        #add cards to deck
        for i in range(0,5):
            self.deck[self.tgen.generate()] += 1
        

    #adds card to deck
    def add_card(self, n):
        self.deck[n] += 1

    """
    def draw_cards(self, n, m):
        if n >= 0 and n < 5:
            self.deck[self.drawd.draw_visible(n)] += 1
        else: self.deck[self.drawd.draw_hidden()] += 1

        if m >= 0 and m < 5:
            self.deck[self.drawd.draw_visible(m)] += 1
        else: self.deck[self.drawd.draw_hidden()] += 1
    """
