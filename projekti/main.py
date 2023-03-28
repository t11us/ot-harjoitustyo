from traindeck  import *
from traingenerator import *

def main():
    tgen = TrainGenerator()
    tdeck = TrainDeck(tgen)
    print(["R","O","Y","G","b","P","B","W","L"])
    print(tdeck.string())
    


if __name__ == "__main__":
    main()