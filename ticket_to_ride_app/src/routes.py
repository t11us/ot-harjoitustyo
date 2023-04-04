lengths = {(1,2):1,(1,4):2,(1,5):3,(1,3):4,(3,5):5,(4,9):6,(5,9):7,(3,4):8}
colors = {(1,2):1,(1,4):2,(1,5):3,(1,3):4,(3,5):5,(4,9):6,(5,9):7,(3,4):0}
bought = {(1,2):0,(1,4):0,(1,5):0,(1,3):0,(3,5):0,(4,9):0,(5,9):0,(3,4):0}

class Routes:
    def __init__(self):
        self.lengths = lengths
        self.colors = colors
        self.bought = bought

    def get_route(self, s1, s2):
        if (s1,s2) in self.lengths.keys():
            return [self.lengths[(s1,s2)], self.colors[(s1,s2)], self.bought[(s1,s2)]]
        else:
            return False

        
    def buy_route(self, s1, s2):
        if self.lengths[(s1,s2)] and self.bought[(s1,s2)] == 0:
            self.bought[(s1,s2)] = 1
            return True
        else:
            return False
