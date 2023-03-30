#test code for Rank.py

from Rank import *
import Deck

#initialize vars, deck
loop = True
cards = []
deck = Deck.Deck()
suitKey = ['s', 'h', 'c', 'd']
suitDict = dict(zip(suitKey, deck.getSuit()))
rankKey= [['a', 'A', 'ace', 'Ace'], ['k','K','king', 'King'], ['q','Q','queen','Queen'],['j','J','jack','Jack'],['10', 'ten'],['9', 'nine'],['8','eight'],['7','seven'],['6','six'],['5', 'five'], ['4','four'], ['3','three'], ['2','two']]
rankKey.reverse()

#create rank dictionary
rankDict = {}
#create dictionary entry map each rankKey to correct entry in deck.rank
for i in range(len(deck.getRank())):
    for k in rankKey[i]:
        rankDict.update({k:deck.getRank()[i]})
'''
print(suitDict)
print()
print(rankDict)
'''
while loop:
    prompt = input(
    '''
    Enter '0' to draw and rank a random hand.
    Enter '1' to rank custom hand.
    Anything else will exit.
    '''
    )
    if prompt != '0' and prompt != '1':
        loop = False
    else:
        if prompt == '0':
            #create & print hand
            for i in range(0,5):
                cards.append(deck.draw())
                print(cards[i].getAsStr(), end = ', ')
            
                
        
        #create specified hand
        elif prompt == '1':
            #get user input
            hand_string=input(
            '''
            Specify 5 card hand. 
            Format as: <rank><suite>, <rank><suite>, <rank><suite>, <rank><suite>, <rank><suite>, 
            rank codes: a, k q j, 10, 9, 8, 7, 6, 5, 4, 3, 2
            Suit codes: c, s, d, h
            '''
            )
            #covert to valid card
            #remove spaces
            clean_hand_string = hand_string.replace(" ", "")
            #print("hand string ="+clean_hand_string)
            #split string
            hand_string_list = clean_hand_string.split(',')
            
            #check len == 5
            if len(cards)!=5:
                #covert each string to card 
                #remove whitespace
                for s in hand_string_list:
                    #s.replace(" ", "")
                    #debuging prints
                    '''
                    print(s)
                    print(s[:-1])
                    print(s[-1])
                    '''
                    #add to cards
                    ca = Card.Card(rankDict.get(s[:-1]), suitDict.get(s[-1]))
                    #print(ca.getAsStr())
                    #cards.append(Card.Card(rankDict.get(s[:-1]), suitDict.get(s[-1])))
                    cards.append(ca)
                for c in cards:
                    print(c.getAsStr(), end = ', ')
                print()

            else:
                print("Error, lenght != 5")            

        print(rankHand(cards))
        for c in cards:
            print(c.getAsStr(), end = ', ')
        print()
        #clear list
        cards.clear()
