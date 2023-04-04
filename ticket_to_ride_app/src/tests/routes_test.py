import unittest

from routes import Routes

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.route = Routes()

    #Testataan setup-asiat
    def test_get_route_returns_false_if_doesnt_exist(self):
        self.assertEqual(self.route.get_route(1,16), False)
    
    def test_get_route_returns_right_things(self):
        self.assertEqual(self.route.get_route(1,2), [1, 1, 0])
    
    def test_buy_routes_works(self):
        self.route.buy_route(1,2,1)
        self.assertEqual(self.route.get_route(1,2)[2], 1)