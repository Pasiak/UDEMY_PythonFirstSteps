for i in range(10):
    print(i)

list = list(range(10))
print("List : ", list, type(list))

print(list[1::])

#LAB

colours = ["red", "orange", "green", "violet", "blue", "yellow"]

def ColourCategory (colours,numberOfColours):
    usedColours = colours[:numberOfColours]
    return usedColours

print(ColourCategory(colours,5))

for colour in colours:
    for colour2 in colours:
        print(colour,colour2,sep=" ")
