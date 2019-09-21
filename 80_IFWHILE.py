values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i = 0
max = len(values)-2

while i<max:
    print(i,values[i],values[i+1],values[i+2])
    
    if values[i]<values[i+1] and values[i+1] < values[i+2]:
        print("\tZnaleziono!",values[i],values[i+1],values[i+2])

    i+=1

    
#LAB
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers)-2

while i<max:
    if numbers[i] * numbers[i] == numbers[i+1]:
    print("Mamy to ",numbers[i], "*", numbers[i], "=" numbers[i+1])
