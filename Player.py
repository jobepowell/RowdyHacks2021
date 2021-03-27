import Card

class Player:
    def __init__(self, startBalance):
        self.balance = startBalance
        self.hand = []
    
    #add card to hand
    def addCard(self, card):
        self.hand.append(card)

    #discard 1 instance of card if found in hand
    def discardCard(self, card):
        for a in self.hand:
            if a == card:
                self.hand.remove(card)
                return
    
    #discard whole hand
    def discardHard(self):
        self.hand.clear();

    #get the value of hand
    def getHand(self):
        return self.hand

    #add to balance
    def addBalance(self, amount):
        self.balance += amount

    #subtract amount from balance
    def subBalance(self, amount):
        self.balance -= amount


        
