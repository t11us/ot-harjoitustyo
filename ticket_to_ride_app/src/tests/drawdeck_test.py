import unittest
    
from traingenerator import TrainGenerator
from traindeck import TrainDeck
from drawdeck import DrawDeck

class TestDrawDeck(unittest.TestCase):
    def setUp(self):
        self.tgen = TrainGenerator()
        self.drawd = DrawDeck(self.tgen)
        

    #Test drawing
    def test_you_can_draw_from_hidden(self):
        n = self.drawd.draw_hidden()
        self.assertGreaterEqual(n, 0)
        self.assertLess(n,9)
    
    def test_you_can_draw_from_visible(self):
        n = self.drawd.draw_visible(0)
        m = self.drawd.draw_visible(self.tgen.colornum-2)
        self.assertGreaterEqual(n, 0)
        self.assertLess(n,9)
        self.assertGreaterEqual(m, 0)
        self.assertLess(m,9)
    