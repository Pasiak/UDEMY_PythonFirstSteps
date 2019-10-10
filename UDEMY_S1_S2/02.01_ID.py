a=b=c=[1,2,3]


print('Value :',a,'\tId :',id(a))
print('Value :',b,'\tId :',id(b))
print('Value :',c,'\tId :',id(c))
a.append(4)
print('Value :',a,'\tId :',id(a))
print('Value :',b,'\tId :',id(b))
print('Value :',c,'\tId :',id(c))
x = 10
y = 10

print(id(x))
print(id(y))
y=y+1-1
print(id(y))
