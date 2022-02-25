import Card

class Player:
    def __init__(self, startBalance):
        self.balance = startBalance
        self.hand = []
        self.active = True
    
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
            bet = input("Enter an amount to bet or press f to fold ")
            if bet == "f" or bet.isdigit():
                return bet
            else:
                print("Invalid input")
