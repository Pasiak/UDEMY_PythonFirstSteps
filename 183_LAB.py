# 183 LAB

import os
line = input("Please enter your next UDEMY Python course price : ")
path = input("Enter path to your .txt file : ")


try:
    with open (path,'w') as file:
        value = int(line)
        file.write(value)
        print('the saved value is :', value)
except FileNotFoundError:
    
        print('File was not found')
except ValueError as e:
    
        print('Sorry you need to enter an integer number ',e)
        
except:
        print('sys.exc_info()[0]')
