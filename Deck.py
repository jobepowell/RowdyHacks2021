import Card
class Deck:
   def __init__(self):
        suit = ["Club", "Diamond", "Spade", "Heart"]
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
        for s in suit:
            for r in rank:
                card = Card.Card(r, s)
                self.cards = {card : True}
 


