import random
print("one random number:",random.randint(1,100))   # 1<= N <= 100
print("\n")

print("Chosing random number from a range:",random.choice(range(1,100)))
print("\n")

print("Chosing random number from a range - easier:",random.randrange(1,100))
print("\n")

list=['John','Ann','Peter','Suzan']
random.shuffle(list)
print(list)
print("\n")

print('Just a random float:',random.random())
print("\n")

##for i in range(0,10):
##    print("random number:",random.randint(1,100))


#LAB

number1 = random.randint(1,100)
print("First number is:'",number1)
number2 = 0
i=0
while  number1 != number2:
    number2 = random.randint(1,100)
    i+=1
    print(i , ":  ",number2)
print("We have match",i,"attempt. Number: ",number2)



# World CUP 2459

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
 
groupNumber = 0
 
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])
