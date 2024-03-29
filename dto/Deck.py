from dto import Card
import random
class Deck:

    def __init__(self):
        self.cards = {}
        #spade, heart, club, diamond
        self.suit = ['\u2664', '\u2661', '\u2667', '\u2662']
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for s in self.suit:
            for r in self.rank:
                card = Card.Card(r, s)
                self.cards[card] = True

    def getSuit(self): #self explanitory
        return self.suit

    def getRank(self): #self explanitory
        return self.rank

    def draw(self): #Returns a card and removes it from the deck
        while True:
            dcard, value = random.choice(list(self.cards.items()))
            if value == True: #False if the card has already been drawn and is no longer in the deck
                self.cards[dcard] = False
                return dcard
    def reset(self): #Sets all the cards value to TRUE, meaning all the cards are in the deck
        for x in self.cards:
            self.cards[x] = True

