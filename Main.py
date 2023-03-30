import Deck
import Card
import Player
import Game
#import Hand

#TEST CODE
"""
#Before Game Setup
#potSize = 0 #Size of the current pot
deck = Deck.Deck()
#playerHand = Hand.Hand(deck.draw(),deck.draw())
#print(playerHand.card1.rank + " of " + playerHand.card1.suit + " and " + playerHand.card2.rank + " of " + playerHand.card2.suit)

#init player1 with 500 balance
player1 =  Player.Player(500)

#give player1 2 rand cards
for i in range(0,2):
    player1.addCard(deck.draw())

#show player1 hand
for i  in range(0,2):
    print(player1.hand[i].rank+" "+player1.hand[i].suit, end = ", ")
print()
"""

#test code for Game class
myGame = Game.Game()
myGame.addPlayer(500)
print("added Player")
while input("enter 'exit' to exit game\n")!="exit":
    myGame.playHand()
