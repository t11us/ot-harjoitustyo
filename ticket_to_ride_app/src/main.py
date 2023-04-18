from traindeck  import *
from traingenerator import *
from routes import *
from drawdeck import *

def main():
    tgen = TrainGenerator()
    routes = Routes()
    ddeck = DrawDeck(tgen)

    ps = int(input("Number of players: "))
    decklist = []
    for i in range(0,ps):
        decklist.append(TrainDeck(tgen))
        
    turn = 0
    while True:
        if turn > len(decklist)-1:
            turn = 0
        print("Player ", turn, "'s turn")
        print("Your deck: ", decklist[turn].deck)
        print("Visible draw cards: ", ddeck.visible)
        action = input("d: draw card, b: build, r: new routes ")

        #code for drawing cards
        if action == "d":
            h = 0
            while True:
                print("Visible draw cards: ", ddeck.visible)
                which = input("h: choose hidden, 0-2: choose visible ")
                if which == "h":
                    decklist[turn].add_card(ddeck.draw_hidden())
                    h += 1
                else:
                    card = ddeck.draw_visible(int(which))
                    if h == 1 and card == tgen.colornum-1:
                        print("illegal choice")
                        continue
                    elif card == tgen.colornum-1:
                        decklist[turn].add_card(card)
                        h += 2
                    else: 
                        decklist[turn].add_card(card)
                        h += 1
                if h == 2:
                    break                   
                    
        
        else:
            print("This action has not been implemented yet")
        
        turn += 1


if __name__ == "__main__":
    main()