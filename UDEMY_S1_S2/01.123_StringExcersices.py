line = "this IS a very STRANGE text"
print(line)
print(line.capitalize())
print(line.title())
print(line.upper())
print(line.lower())
print(line.swapcase())
print(line.casefold())
print(line.count('e'))
print(line.find('e'))
print(line.rfind('e'))
print(line.index('e')) 
print(line.rindex('e')) 
print("s" in line)
print(line.startswith('this')) 
print(line.endswith('text'))


print(line.split())
list = line.split()
newString = ' '.join(list)
print(newString)
print("-----------------------------------------")


#LAB


poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

lines = poem.split("\n")
i=0
for i in range(8):
    print(lines[i])
    print(lines[i+8])
