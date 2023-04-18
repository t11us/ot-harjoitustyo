import unittest

from routes import Routes

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.route = Routes()

    #testing get_route()
    def test_get_route_returns_false_if_doesnt_exist(self):
        self.assertEqual(self.route.get_route(1,16), False)
    
    def test_get_route_returns_right_things(self):
        self.assertEqual(self.route.get_route(1,2), [1, 1, 0])

    #testing buy_route()  
    def test_buy_route_changes_belongs(self):
        self.route.buy_route(1,2,1)
        self.assertEqual(self.route.get_route(1,2)[2], 1)

    def test_buy_route_owned_returns_false(self):
        self.route.buy_route(1,2,1)
        self.assertEqual(self.route.buy_route(1,2,1), False)
    
    def test_buy_non_extant_route_returns_false(self):
        self.assertEqual(self.route.buy_route(1,16,1), False)