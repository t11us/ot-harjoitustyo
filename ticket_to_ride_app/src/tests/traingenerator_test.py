import unittest
    
from traingenerator import TrainGenerator

class TestTrainGenerator(unittest.TestCase):
    def setUp(self):
        self.tgen = TrainGenerator()

    #Testataan setup-asiat
    def test_returns_number_in_right_range(self):
        self.assertGreaterEqual(self.tgen.generate(),0)
        self.assertLessEqual(self.tgen.generate(),7)
    