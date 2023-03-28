from traingenerator import TrainGenerator

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

    def string(self):
        return(self.deck)



