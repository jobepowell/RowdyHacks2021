#test code for Rank.py

from Rank import *
import Deck

#initialize vars, deck
loop = True
cards = []
deck = Deck.Deck()

while loop:
    prompt = input(
    '''
    Enter '0' to draw and rank a random hand.
    Anything else will exit.
    '''
    )
    if prompt == '0':
        #create & print hand
        for i in range(0,5):
            cards.append(deck.draw())
            print(cards[i].getAsStr(), end = ', ')
        
        print(rankHand(cards))
        for c in cards:
            print(c.getAsStr(), end = ', ')
            
        print()
        #clear list
        cards.clear()

    else:
        loop = False




