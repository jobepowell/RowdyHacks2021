from dto import Card


class Player:
    def __init__(self, name, startBalance):
        self.name = name
        self.balance = startBalance
        self.hand = []
        self.active = True
        self.handRank = []; # index 0:Highest rank, index 1: type of hand (ie straight, flush, pair)
    
    #add card to hand
    def addCard(self, card):
        self.hand.append(card)

    #discard 1 instance of card if found in hand
    def discardCard(self, card):
        for a in self.hand:
            if a == card:
                self.hand.remove(card)
                return

    #Print's the player's highest rank hand
    def printHandRank(self):
        if self.handRank[1] == "High":
            print(self.handRank[0] + " High")
        elif self.handRank[1] == "Pair" or self.handRank[1] == "Three-of-a-Kind":
            print(self.handRank[1] + " of " + self.handRank[0]+"\'s")
        elif self.handRank[1] == "Flush" or self.handRank[1] == "Straight":
            print(self.handRank[1] + ", " + self.handRank[0] + " high")

    #discard whole hand
    def discardHand(self):
        self.hand.clear()

    #get the value of hand
    def getHand(self):
        return self.hand

    #add to balance
    def addBalance(self, amount):
        self.balance += amount

    #subtract amount from balance
    def subBalance(self, amount):
        self.balance -= amount

    #get user input in single player 
    def getInput(self):
        wait = True
        while(wait):
            bet = input("({}) Enter an amount to bet or press f to fold ".format(self.name))
            if bet == "f" or bet.isdigit():
                return bet
            else:
                print("Invalid input")
