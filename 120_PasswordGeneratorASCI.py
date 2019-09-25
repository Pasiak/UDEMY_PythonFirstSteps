##for i in range (32,127):
##    print(i, chr(i))
import random
ints = range(33,127)
password =""

for i in range(16):
    password += chr(random.choice(ints))
print(password)


#LAB
min=1
max=6

dice = random.randint(min,max)
print(dice)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')
 
print('----------------------')

dices = []
i=0

for i in range(0,5):
    dice = random.randint(min,max)
    dices.append(dice)
dices.sort()   
print(dices)
