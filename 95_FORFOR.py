for x in range(1,6):
    line =str(x)
    for y in range(1,6):
        line+= '\t%3d' %(x*y)
    print(line)


#LAB
print("")
x=10
silnia=1
for i in range(0,x):
    
    silnia = silnia * (i+1)
    print(i+1,"!    ", silnia, sep="")


#LAB 2

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for i in range (0,len(list_noun)):   
    for y in range (0,len(list_adj)):  
        print(list_adj[y],list_noun[i],sep= " ")   
