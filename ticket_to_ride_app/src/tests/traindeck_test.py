import unittest
from traingenerator import TrainGenerator
from traindeck import TrainDeck

class TestTrainDeck(unittest.TestCase):
    def setUp(self):
        self.tgen = TrainGenerator()
        self.tdeck = TrainDeck(self.tgen)


    #Testataan setup-asiat
    def test_rahamaara_oikein(self):
        n = 0
        for d in self.tdeck.deck:
            n += d
        self.assertEqual(n, 5)
    
    