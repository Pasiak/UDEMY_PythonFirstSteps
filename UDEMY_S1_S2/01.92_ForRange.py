for number in range(1,21):
    #print(number)
    if number %2 ==0:
        print('Number %2d is %s' % (number,'even'))
        
    else:
        print('Number %2d is %s' % (number,'odd'))

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for n in range(1,11):
    print(n,string_A)
    print(n,string_B)


for n in range(1,11):
    print(n*"x")
