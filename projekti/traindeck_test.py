import unittest
from traindeck import TrainDeck
from traingenerator import TrainGenerator

class TestTrainDeck(unittest.testCase):
    def setUp(self):
        tdeck = TrainDeck()
        tgen = TrainGenerator()
