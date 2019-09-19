atext = "This is a text"
#print(atext.endswith('ext'))

quote = "A good programer is someone who looks both ways before crossing a one -way street"
print(quote.upper())    #Wyświetl tekst napisany tylko wielkimi literami
print(quote.lower())    #Wyświetl tekst zapisany tylko małymi literami
print(quote.endswith('street'))     #Sprawdź czy tekst kończy się słowem 'street'
print(quote.upper().isupper())      #Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
print(quote.find('one'))            #Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'
print(quote.replace("one","1"))     #Zamień w tekście słowo 'one' na '1'
print(quote.replace("one","1").replace("both","2")) 
print(quote.split(" "))    #Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
print(quote.isalpha())      #Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem zliterami i cyframi

drive = r'c:\\'
folder = r'scripts\\python\\'
file = r'myscript.ph'            #r przed napisaem karze interpretować zmienna jako surowy text 
path = drive+folder+file
print(path)
    
drive1 = 'c:\\'
folder1 = 'scripts\\python\\'       
file1 = 'myscript.ph'
path1 = drive1+folder1+file1
print(path1)
    

















