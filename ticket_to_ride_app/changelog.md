# Changelog

### Week 2
traingenerator.py:
- class TrainGenerator created
- generate() returns a random number between 0 and 8
- has class dicts that map numbers to colors

traindeck.py:
- class TrainDeck created
- contains a list of the cards in the player's hand
- at init gets five random cards from traingenerator

### Week 3
routes.py
- class Routes created
- contains dicts of colors lengths and ownership of extant routes
- get_route() returns info on route between two given stations or returns False if route doesn't exist
- buy_route() changes status of route if bought


### Week 4
main.py
- now asks how many players are playing
- lets players have turns
- lets players draw cards on their turn

traindeck.py
- now places starting cards in deck at init
