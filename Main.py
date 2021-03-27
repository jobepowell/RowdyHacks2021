import Deck
import Card
#Before Game Setup
potSize = 0 #Size of the current pot
deck = Deck.Deck()
thiscard = deck.draw()
print(thiscard.rank + " " + thiscard.suit)
