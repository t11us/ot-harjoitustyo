import random

colornames = {0:"Red", 1:"Orange", 2:"Yellow", 3:"Green", 4:"Blue", 5:"Purple", 6:"Black", 7:"White",8:"L"}
colorletters = ["R","O","Y","G","b","P","B","W"]
colornum = 9

#Class that gives out random train cards
#Will be improved upon later
class TrainGenerator:
    def __init__(self):
        self.colornames = colornames
        self.colorletters = colorletters
        self.colornum = colornum
        pass

    def generate(self):
        i = random.randint(0, self.colornum-1)
        
        return i
        


        