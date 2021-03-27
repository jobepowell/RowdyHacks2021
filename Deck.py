import Card
import random
class Deck:

    def __init__(self):
        self.cards = {}
        suit = ["Club", "Diamond", "Spade", "Heart"]
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for s in suit:
            for r in rank:
                card = Card.Card(r, s)
                self.cards[card] = True

    def draw(self): #Returns a card and removes it from the deck
        while True:
            dcard, value = random.choice(list(self.cards.items()))
            if value == True: #False if the card has already been drawn and is no longer in the deck
                self.cards[dcard] = False
                return dcard
    def reset(self): #Sets all the cards value to TRUE, meaning all the cards are in the deck
        for x in self.cards:
            self.cards[x] = True

