#test code for Rank.py

from Rank import *
import Deck

#initialize vars, deck
loop = True
cards = []
deck = Deck.Deck()
suitKey = ['C', 'D', 'S', 'H']
suitDict = dict(zip(suitKey, deck.getRank()))
while loop:
    prompt = input(
    '''
    Enter '0' to draw and rank a random hand.
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
                rank codes: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
                Suit codes: C, S, H, D 
                '''
            )
            #covert to valid card
            #split string
            hand_string_list = hand_string.split(',')
            
            #check len == 5
            if len(cards)==5:
                #covert each string to card 
                #remove whitespace
                for s in hand_string_list:
                    s.replace(" ", "")
                    #add to cards
                    cards.append(Card.Card(s[:-1], suitDict.get(s[-1])))
                



        print(rankHand(cards))
        for c in cards:
            print(c.getAsStr(), end = ', ')

        print()
        #clear list
        cards.clear()




