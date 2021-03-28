import Deck
import Card
import Player


class Game:

    def __init__(self):
        #initialize 52 card no-order deck
        self.deck = Deck.Deck()
    
        #create list for players
        self.players = []

        #create list of pots
        self.pot = [0]

        #create list for table cards
        self.table = []

        #create list for player bets
        self.playerBets = []

    #initializes player with 0 balance adds player to list
    def addPlayer(self, num):
        self.players.append(Player.Player(num))

    #drops first instance of targetPlayer found in players
    def dropPlayer(self, targetPlayer){
        for p in self.players:
            if p = targetPlayer:
                self.players.drop(p)
                return
   
    def drawFromDeck(player, number):
        for n in range(0, number):
            player.addCard(deck.draw())


    #do a betting round
    def bettingRound(self):
        requiredBet = 0
        i = 0
        stopPoint = -1
        while(i % self.playerBets.count() != stopPoint):
            p = self.playerBets[i % self.playerBets.count()]
            if p[1] != -1:
                action = p[0].getInput()
                if action == "f":
                    self.pot[0] += p[1]
                    p[1] = -1    
                else
                    p[0].balance -= action
                    playerbet[1] += action
                    if p[1] > requiredBet:
                        requiredBet = p[1]
                        stopPoint = i
            if stopPoint = -1:
                stopPoint = 0
            i++          
            


            
    
    #play a hand of poker
    def playHand(self){
        #add players to hand
        for p in self.players:
            if p.active == True:
                self.playerBets.append([p, 0])
                self.drawFromDeck(deck, 2)

        #deal cards to players
        for p in self.players:
            if p.active == True:
        
        #round of betting
        bettingRound()

        #three cards to table
        for i in range(0, 3):
            self.table.append(self.deck.Draw())
        #round of betting
        bettingRound()
 
        #1 card to table
        self.table.append(self.deck.Draw())
        #round of betting
        bettingRound()
         #1 card to table
        self.table.append(self.deck.Draw())
        #round of betting
        bettingRound()
  
        #determine winners and award pot
