import os
import time

##print("Current directory is:", os.getcwd())
##currentDir = os.getcwd()
##filename = 'results.txt'
##fullpath = os.path.join(currentDir,filename)
##print("\nThe constructed file path is: ",fullpath)
##
##relativePath ='output.txt'
##print("\nThe absolute path is :",os.path.abspath(relativePath))
##
##filepath = r"C:\temp\results.txt"
##print("\nThe file name part is :",os.path.basename(filepath))
##print("\nThe directory part is :",os.path.dirname(filepath))
##
##print("\nIs file existing? :",os.path.exists(filepath))
##

dir = input("Please insert path to file ")

isDirExist = os.path.isdir(dir)
if isDirExist == False :
    print("Tis is not a valid path")
    exit()
print("Your path",dir," is valid ", isDirExist)
file = input("Please insert filename ")
path = os.path.join(dir,file)
print(path)

isFileExist = os.path.exists(path)
if isFileExist == False :
    print("File not exist")
    exit()
print("Your file",file," exist ", isFileExist)

print("------------------------------------------")
print("INFORMATION ABOUT FILE :",file)
print("------------------------------------------")
print("------------------------------------------")
print('Last modified date', time.localtime(os.path.getmtime(path)))
print('Size in bytes', os.path.getsize(path))

print('Current directory is: ', os.getcwd())
print('Relative path to the file is', os.path.relpath(path))

