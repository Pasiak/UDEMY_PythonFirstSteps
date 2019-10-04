##filename = r'C:\Users\El Patrico\Desktop\text.txt'
##line = 'Europe'
##cities = ['London','Berlin','Paris','Warsaw','Mardid','Rome']
##
##file = open(filename, 'w')
##file.write(line)
##for city in cities:
##    file.write(city + ' ')
##
##file.close()

#LAB
import os
##webaddreses = []
##line = input("Please, give me a WWW addres: ")
##             
##while line != '':
##    webaddreses.append(line)
##    line = input("Please, give me a WWW addres. Press Enter to exit ")
##dirname  = os.getcwd()
##print("You are in: ",dirname)
##filename = input("Please give me file name")
##filepath = os.path.join(dirname,filename)
##
##file = open(filename, 'w')
##for adres in webaddreses:
##    file.write(adres +"\n")
##file.close()
filename2 = input(
    "Enter file path: ")
while os.path.isfile(filename2) != True:
    print("Wrong path, file does'nt exist")
    filename2 = input("Enter correct file path: ")
webaddreses2 = []

with open(filename2,'r') as file2:
    for line in file2:
        webaddreses2.append(line.replace("\n",''))
        
for line in webaddreses2:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')
