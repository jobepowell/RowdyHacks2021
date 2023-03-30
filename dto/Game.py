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

        # List of players,bets that the player has made
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
        while(i % len(self.playerBets) != stopPoint):
            p = self.playerBets[i % len(self.playerBets)]
            if p[1] != -1:
                action = p[0].getInput()
                if action == "f":
                    self.pot[0] += p[1]
                    p[1] = -1
                else:
                    p[0].balance -= int(action)
                    self.playerBets[i][1] += int(action)
                    self.pot[0] += int(action)
                    if p[1] > requiredBet:
                        requiredBet = p[1]
                        stopPoint = i
            if stopPoint == -1:
                stopPoint = 0
            i+=1



    #play a hand of poker
    def playHand(self):
        # Flop
        self.dealPlayers()
        self.bettingRound()
        self.drawCard(3)
        self.printHand()
        self.printTable()

        # Turn
        self.bettingRound()
        self.drawCard(1)
        self.printHand()
        self.printTable()
        self.bettingRound()

        # River
        self.drawCard(1)
        self.printHand()
        self.printTable()
        self.bettingRound()

        # End-Game
        self.decideWinner()
        self.resetTable()

    def drawCard(self, numCards):
        for i in range(0, numCards):
            self.table.append(self.deck.draw())

    def dealPlayers(self):
        for p in self.players:
            if p.active == True:
                self.playerBets.append([p, 0])
                self.drawFromDeck(p, 2)

    def printTable(self):
        print("On the table: ")
        for i in self.table:
            print("| " + i.rank + " " + i.suit, end=" | ")
        print()
        print("pot: "+ str(self.pot))
        print()

    def printHand(self):
        print("Your hand: ")
        for i in self.players[0].hand:
            print("| " + i.rank + " " + i.suit, end=" | ")
        print()

    def resetTable(self):
        for p in self.playerBets:
            p[0].discardHand()
        self.table.clear()
        self.deck.reset()

    def decideWinner(self):
        for p in self.players:
            currHand = self.table.copy()
            currHand.extend(p.hand)
            p.handRank = Rank.rankHand(currHand)
            p.printHandRank()
