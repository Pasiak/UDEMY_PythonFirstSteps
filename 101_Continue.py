persons = ['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svietlana@mycompany.eu']
domain = 'mycompany.com'

##emails = []
##
##for person in persons:
##    if '@' in person:
##        emails.append(person)
##    else:
##        email = person+'@'+domain
##        emails.append(email)
##for email in emails:
##    #print(email)


#Another solution with cointinue
    
emails = []
for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    
    email = person+'@'+domain
    emails.append(email)

for email in emails:
    print(email)


#LAB
##
##    menu = '''
##Choose what you want me to do for you:
##1 - COFFEE
##2 - TEA
##3 - MAKE ME SMILE
##---------------
##To stop this script select 0
##'''
## 
##smile = '''
## 
##                          oooo$$$$$$$$$$$$oooo
##                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
##                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
##   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
##oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
##"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
##  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
##  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
##   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
##    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
##   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
##   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
##  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
##  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
## """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
##            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
##              $$$o          "$$""$$$$$$""""           o$$$
##               $$$$o                                o$$$"
##                "$$$$o      o$$$$$$o"$$$$o        o$$$$
##                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
##                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
##                        ""$$$$$$$oo $$$$$$$$$$
##                                """"$$$$$$$$$$$
##                                    $$$$$$$$$$$$
##                                     $$$$$$$$$$"
##                                      "$$$""""
##'''
##i=1
##while i==1:
##    print(menu)
##    letter = input()
##
##    if letter =='1':
##        print('Function COFFEE not implemented. Please press ENTER')
##        enter = input()
##        continue
##    
##    elif letter == "2":
##        print('Function TEA not implemented. Please press ENTER')
##        enter = input()
##        continue
##    
##    elif letter == "3":
##        print('Please press ENTER')
##        print(smile)
##        enter = input()
##        continue
##    
##    elif letter == "0":
##        break
##    
##    else:
##        print("You need to make a valid choice. Press ENTER and try again!")
##        enter = input()
##        continue
print('-----------------------------------------------')
    
                                    #LAB2
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
i=0

while i < maxTimeYears:
    odsetki = initialCapital * percent
    initialCapital += odsetki
    i+=1
    print(" W roku %d odsetki wynosza %d a kapitał to %d" % (i,odsetki,initialCapital))
    continue
print('-----------------------------------------------')                                    
                        #LAB3
fibonacciIterations=20
a1=0
a2=1
a3 = 0

while i <= fibonacciIterations:
    a3 = a1+a2  
    i+=1
    print(a3)
    a1=a2
    a2=a3
print('-----------------------------------------------')    
    
#LAB 4
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}

for word in dictionary.keys():
    print(word,'-',dictionary[word])

    
print('-----------------------------------------------')

    
