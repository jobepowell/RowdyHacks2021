from dto import Card

#import operator

handValueDict = {
    8 : "Straight Flush",
    7 : "Four-of-a-Kind",
    6 : "Full House",
    5 : "Flush",
    4 : "Straight",
    3 : "Three-of-a-Kind",
    2 : "Two Pair",
    1 : "Pair", 
    0 : "High"
}

rankValue = {
    '2' : 0,
    '3' : 1,
    '4' : 2,
    '5' : 3,
    '6' : 4,
    '7' : 5,
    '8' : 6,
    '9' : 7,
    '10' : 8,
    'J' : 9,
    'Q' : 10,
    'K' : 11,
    'A' : 12,
}

def getRankFromRankVal(r):
    for key,value in rankValue.items():
        if r == value:
            return key

#Given list of Cards, determine highest ranking poker hand
#return int coresponding to that hand
def rankHand(cards):
    handVal = -1
    ranks = []  #list that holds ranks
    suits = []  #list that holds suits
    #sort hand from highest to lowest rank
    cards.sort(key = lambda card: rankValue[card.rank] , reverse = True)
    # list of cards ranks converted from rankValues dictionary
    rankVals = [rankValue[o.rank] for o in cards] 
    #calucalte mode magnitue
    for card in cards:
        ranks.append(card.rank)
        suits.append(card.suit)
    modeRank = max(ranks, key=ranks.count)
    modeSuit = max(suits, key=suits.count)
    
    #determine if is a straight
    for r in rankVals:
        if r-1 in rankVals and r-2 in rankVals and r-3 in rankVals and r-4 in rankVals:
            #set straight
            if(handVal < 4):
                handVal = 4
                print("is stright") 
        

    #determine if is a flush
    if suits.count(modeSuit) >= 5: #Flush if 5 cards of same suit
        for i in range(len(cards)): #Finds the highest card of the flush's suit
            if cards[i].getSuit() != modeSuit:
                break
            else:
                if i == len(suits)-1:
                    print("is Flush")
                    if handVal == 4: #straight 
                        handVal = 8 #set to straight flush
                    else:
                        handVal = 5 #set to flush

    #test print
    print("Ranks:", end=': ') 
    for r in ranks:
        print(r, end=',')
    print()

     
    if ranks.count(modeRank) == 4:#check for 4-of-a-kind
        if handVal<7:
            handVal=7
    if ranks.count(modeRank) == 3: #check if there are max 3 cards of same rank
        if ranks.count(ranks[3])==2:
            if handVal < 6:
                handVal = 6
        if handVal < 3:
            handVal = 3
    elif ranks.count(modeRank) == 2: #check if there are max 2 cards of same rank
        if (ranks.count(ranks[2])) == 2:
            handVal=2
        if handVal < 1:
            handVal = 1
    elif ranks.count(modeRank) == 1:   #check if there are max 1 chard of same rank
        if handVal < 0:
            handVal = 0

    return [str(modeRank), handValueDict[handVal]]
