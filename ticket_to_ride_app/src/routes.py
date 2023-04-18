

class Routes:
    def __init__(self):
        #random routes for testing purposes
        self.lengths = {(1,2):1,(1,4):2,(1,5):3,(1,3):4,(3,5):5,(4,9):6,(5,9):7,(3,4):8}
        self.colors = {(1,2):1,(1,4):2,(1,5):3,(1,3):4,(3,5):5,(4,9):6,(5,9):7,(3,4):0}
        self.belongs = {(1,2):0,(1,4):0,(1,5):0,(1,3):0,(3,5):0,(4,9):0,(5,9):0,(3,4):0}

    #returns info on a route
    def get_route(self, s1, s2):
        if (s1,s2) in self.lengths.keys():
            return [self.lengths[(s1,s2)], self.colors[(s1,s2)], self.belongs[(s1,s2)]]
        else:
            return False

    #changes route's value in belongs if available
    def buy_route(self, s1, s2, player):
        if (s1,s2) in self.lengths.keys() and self.belongs[(s1,s2)] == 0:
            self.belongs[(s1,s2)] = player
            return True
        else:
            return False
