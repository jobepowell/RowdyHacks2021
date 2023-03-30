from dto import Deck, Card, Rank, Player


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
    def dropPlayer(self, targetPlayer):
        for p in self.players:
            if p == targetPlayer:
                self.players.drop(p)
                return

    def drawFromDeck(self, player, number):
        for n in range(0, number):
            player.addCard(self.deck.draw())


    #do a betting round
    def bettingRound(self):
        requiredBet = 0
        i = 0
        stopPoint = -1
        #while stop point has not been reached
        while(i % len(self.playerBets) != stopPoint):
            #p set to current betting player
            p = self.playerBets[i % len(self.playerBets)]
            #if p is a vallid bettor
            if p[1] != -1:
                #get input from current betting player
                action = p[0].getInput()
                #if current player folds
                if action == "f":
                    #currant player's bets are added to pot
                    self.pot[0] += p[1]
                    #current player is no longer a valid bettor 
                    p[1] = -1
                else:
                    #current player's bet is duducted from the ballance
                    p[0].balance -= int(action)
                    #player's bet is added to their amount bet 
                    self.playerBets[0][1] += int(action)
                    #if bt is greater than required bet
                    if p[1] > requiredBet:
                        #requred bet set 
                        requiredBet = p[1]
                        #stop point is now set to the current player
                        stopPoint = i
            #stopPoint intially set to -1 to avoid initial check of <if 0 !=0>
            if stopPoint == -1:
                stopPoint = 0
            i+=1

    #play a hand of poker
    def playHand(self):
        #add players to hand
        for p in self.players:
            if p.active == True:
                self.playerBets.append([p, 0])
                self.drawFromDeck(p, 2)
        """
        #deal cards to players
        for p in self.players:
            if p.active == True:
               self.drawFromDeck(p, 2)    
        """
        #round of betting
        self.bettingRound()

        #three cards to table
        for i in range(0, 3):
            self.table.append(self.deck.draw())
        print("Your hand: ")
        for i in self.players[0].hand:
            print("| " + i.rank + " " + i.suit, end=" | ")

        print("pot: "+str(self.pot))

        print()
        print("On the table: ")
        for i in self.table:
            print("| " + i.rank + " " + i.suit, end=" | ")
       
        print()

        #round of betting
        self.bettingRound()

        #1 card to table
        self.table.append(self.deck.draw())
        print("Your hand: ")
        for i in self.players[0].hand:
            print("| " + i.rank + " " + i.suit, end=" | ")
        print()
        print("On the table: ")
        for i in self.table:
            print("| " + i.rank + " " + i.suit, end=" | ")
        print()
        #round of betting
        self.bettingRound()
         #1 card to table
        self.table.append(self.deck.draw())
        print("Your hand: ")
        for i in self.players[0].hand:
            print("| " + i.rank + " " + i.suit, end=" | ")
        print()
        print("On the table: ")
        for i in self.table:
            print("| " + i.rank + " " + i.suit, end=" | ")
        print()
        #round of betting
        self.bettingRound()
        for p in self.players:
            currHand = self.table.copy()
            currHand.extend(p.hand)
            p.handRank = Rank.rankHand(currHand)
            p.printHandRank()
        #determine winners and award pot

        #reset game
        for p in self.playerBets:
            p[0].discardHand()
        self.table.clear()
        self.deck.reset()
                

