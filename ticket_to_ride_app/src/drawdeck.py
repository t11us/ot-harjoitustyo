from traingenerator import TrainGenerator

class DrawDeck:
    def __init__(self, traingenerator):
        self.tgen = traingenerator

        self.visible = []
        #for i in range(0,5):
        for i in range(0,self.tgen.colornum-1):
            self.visible.append(self.tgen.generate())
    

    #takes a card from the visible array
    def draw_visible(self, n):
        value = self.visible[n]
        self.visible[n] = self.tgen.generate()
        return value
    
    #takes a card from the hidden deck
    def draw_hidden(self):
        return self.tgen.generate()
