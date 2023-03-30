class Card:
    def __init__(self,r,s):
        self.rank = r
        self.suit = s

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    #return card as a string
    def getAsStr(self):
        return self.rank + " " + self.suit
