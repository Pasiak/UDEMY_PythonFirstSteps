import os
path = r"C:\Users\El Patrico\Desktop\tempTXT\02.13.txt"

def howManyWordsInSentense(path):
    counter = 0
    with open(path, "r") as file:
        for line in file:
            words = line.split(" ")
            print(words)
            counter = len(words) + counter
    return counter

if os.path.isfile(path):
    print(howManyWordsInSentense(path))
else:
    print("File not exsitst")
