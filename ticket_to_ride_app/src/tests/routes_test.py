import unittest

from routes import Routes

class TestTrainGenerator(unittest.TestCase):
    def setUp(self):
        self.route = Routes()

    #Testataan setup-asiat
    def test_get_route_returns_false_if_doesnt_exist(self):
        self.assertEqual(self.route.get_route(1,16), False)
    