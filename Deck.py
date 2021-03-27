import Card
import random
class Deck:
    def __init__(self):
        card = Card.Card('King','Clubs')
        self.cards = {card : True} #True meaning that the card IS IN the deck

    def draw(self):
        while True:
            dcard, value = random.choice(list(self.cards.items()))
            if value == True: #False if the card has already been drawn and is no longer in the deck
                self.cards[dcard] = False
                return dcard



