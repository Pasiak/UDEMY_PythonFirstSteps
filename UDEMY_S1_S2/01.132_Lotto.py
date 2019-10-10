import random
##
##myNumbers =[]
##while len(myNumbers) < 7:
##    newNumber = random.randint(1,49)
##    
##    if newNumber in myNumbers:
##        print(newNumber, "Wylosowano już taki numer - Losujemy raz jeszcze")
##    else:
##        print("Wylosowana liczba to",newNumber)
##        myNumbers.append(newNumber)
##
##print(myNumbers)
##
##
##
###LAB
##colors = ['Hearts','Diamonds','Clubs','Spades']
##
##figures = ['Ace','King','Queen','Jack','10','9']
##
##allCards = []
##
##for color in colors:
##    for figure in figures:
##        allCards.append(color+" "+figure,)
###print(allCards)
##random.shuffle(allCards)
##print("--------------------------Shuffled Cards---------------")
##print(allCards)
##
##player1 = []
##player2 = []
##i=0
##for card in allCards:
##    if i%2 == 0:
##        player1.append(card)
##    else:
##        player2.append(card)
##    i+=1 
##    
##print("--------------------------Player1 cards ---------------")
##print(player1)
##print("--------------------------Player2 cards ---------------")
##print(player2)




#LAB GAME

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
i=0
for card in allCards:
    if i%2 == 0:
        player1.append(card)
    else:
        player2.append(card)
    i+=1
print("--------------------------Player1 cards ---------------")
print(player1)
print("--------------------------Player2 cards ---------------")
print(player2)

while len(player2) >0 and len(player1) >0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print("Player 1 card is",card1)
        print("Player 2 card is",card2)
        print("Player 1 WIN!!!")
        print("-------------------------------------------")
        print("Player 1 has : ",len(player1)," cards")
        print("Player 2 has : ",len(player2)," cards")
        input()
        continue
    elif card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
        print("Player 1 card is",card1)
        print("Player 2 card is",card2)
        print("Nobody Win!!!")
        print("-------------------------------------------")
        print("Player 1 has : ",len(player1)," cards")
        print("Player 2 has : ",len(player2)," cards")
        input()
        continue
    elif card1['Power'] < card2['Power']:
        player2.append(card1)
        player2.append(card2)
        print("Player 1 card is",card1)
        print("Player 2 card is",card2)
        print("Player 2 WIN!!!")
        print("-------------------------------------------")
        print("Player 1 has : ",len(player1)," cards")
        print("Player 2 has : ",len(player2)," cards")
        input()
        continue
