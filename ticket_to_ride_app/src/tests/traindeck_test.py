import unittest
from traingenerator import TrainGenerator
from traindeck import TrainDeck
from drawdeck import DrawDeck

class TestTrainDeck(unittest.TestCase):
    def setUp(self):
        self.tgen = TrainGenerator()
        self.drawd = DrawDeck(self.tgen)
        self.tdeck = TrainDeck(self.tgen)


    #Testataan setup-asiat
    def test_length_correct(self):
        n = 0
        for d in self.tdeck.deck:
            n += d
        self.assertEqual(len(self.tdeck.deck), self.tgen.colornum)
    
    def test_cards_added_to_deck(self):
        n = self.tdeck.deck[0]
        self.tdeck.add_card(0)
        self.assertEqual(self.tdeck.deck[0], n+1)


