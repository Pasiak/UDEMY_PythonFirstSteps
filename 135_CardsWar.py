colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
 
allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
 
import random
 
random.shuffle(allCards)
print(allCards)
 
player1 = []
player2 = []
cardDecided1 = []
cardDecided2 = []
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 1--------')
print(player2)    
 
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
 
    if card1["Power"] == card2["Power"]:
        
        #print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=!!!!!!!!!!WAR!!!!!!!!! \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
        cardUseles1 = player1.pop(1)
        cardUseles2 = player2.pop(1)
        cardDecided1 = player1.pop(2)
        cardDecided2 = player2.pop(2)
        print("-----------------------------------")
        print('Useless cards are: \t %d \t %d \t' % (cardUseles1["Power"], cardUseles2["Power"]))
        print('decided cards in this battle: \t %d \t %d \t' % (cardDecided1["Power"], cardDecided2["Power"]))
        
        if cardDecided1["Power"] > cardDecided2["Power"]:
                print("Elo")
                player1.append(card1)
                player1.append(card2)
                player1.append(cardUseles1)
                player1.append(cardUseles2)
                player1.append(cardDecided1)
                player1.append(cardDecided2)
                print("Player1 WON taking everything!",len(player1)*'*')
                input()
        elif cardDecided1["Power"] < cardDecided2["Power"]:
                player2.append(card1)
                player2.append(card2)
                player2.append(cardUseles1)
                player2.append(cardUseles2)
                player2.append(cardDecided1)
                player2.append(cardDecided2)
                print("Player2 WON taking everything!",len(player2)*'*')
                input()
        elif cardDecided1["Power"] == cardDecided2["Power"]:
                print("No win")
                player1.append(card1)
                player2.append(card2)
                player1.append(cardUseles1)
                player2.append(cardUseles2)
                player1.append(cardDecided1)
                player2.append(cardDecided2)


        
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        #print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        #print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
 
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')
