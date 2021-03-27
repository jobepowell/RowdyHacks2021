import Deck
import Card
import Hand
#Before Game Setup
potSize = 0 #Size of the current pot
deck = Deck.Deck()
playerHand = Hand.Hand(deck.draw(),deck.draw())
print(playerHand.card1.rank + " of " + playerHand.card1.suit + " and " + playerHand.card2.rank + " of " + playerHand.card2.suit)
