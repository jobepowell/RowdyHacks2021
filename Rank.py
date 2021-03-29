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
#Given list of Cards, determine highest ranking poker hand
#return int coresponding to that hand
def rankHand(cards):
    #sort hand from highest to lowest rank
    cards.sort(key = lambda card: rankValue[card.rank] , reverse = True)
    #calucalte mode magnitue
    #determine if is a straight
    #determine if is a flush
    #if straight AND flush
    #if mag(mode) = 3
        #determine if pair in other cards
    #if magnitute(mode) < 3 AND !straight AND !flush
        #if magnitude(mode) = 2
            #determine if two pair
            
    return -1
