cargo = [40,20,1,2,30,5,2,7,3,16,32,40,20,35,15,32,9]
boxCapacity = 90
box = []
i = 0


while i<len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1


print("The colected items sum is:",sum(box))
print("The elements are:",box)


#LAB

i=0

##while i<=50:
##    print(i+(i+1))
##    i+=1
##    

import random
my_number = random.randint(0,20)
guess =-1
trials =0

print("Guess my number")
guess = int(input())
while my_number != guess:
    print("Wrong guess my nuber again")
    guess = int(input())
    trials+=1
else:
    print("Brawo wylosowana liczba to",my_number, "Liczba prób ",trials+1)
