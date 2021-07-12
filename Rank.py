import Card
#import operator

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
    ranks = []
    suits = []
    #sort hand from highest to lowest rank
    cards.sort(key = lambda card: rankValue[card.rank] , reverse = True)
    rankVals = [rankValue[o.rank] for o in cards] # list of cards ranks converted via rankValues dictionary
    #calucalte mode magnitue
    for card in cards:
        ranks.append(card.rank)
        suits.append(card.suit)
    modeRank = max(ranks, key=ranks.count)
    modeSuit = max(suits, key=suits.count)
    #determine if is a straight
    for r in rankVals:
        if r-1 in rankVals and r-2 in rankVals and r-3 in rankVals and r-4 in rankVals:
            return [str(getRankFromRankVal(r)),"Straight"]

    #determine if is a flush
    if suits.count(modeSuit) >= 5: #Flush if 5 cards of same suit
        for card in cards: #Finds the highest card of the flush's suit
            if card.suit == modeSuit:
                return[str(card.rank),"Flush"]
    #if straight AND flush

    if ranks.count(modeRank) == 4:
        return [str(modeRank), "Three-of-a-Kind"]
    if ranks.count(modeRank) == 3:
        return [str(modeRank),"Three-of-a-Kind"]
    elif ranks.count(modeRank) == 2:
        return [str(modeRank), "Pair"]
    elif ranks.count(modeRank) == 1:
        return [str(modeRank), "High"]

    return -1
