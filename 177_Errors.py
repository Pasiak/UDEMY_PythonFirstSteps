import sys
tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many persons are in the team? ')
    persons = int(personsStr)

    tasksPerPerson = tasks / persons
##except:
##    print("Something went wrong....",sys.exc_info()[0])
except ZeroDivisionError as e:
    print('Sorry - you need to enter value > 0 ',e)
    
except ValueError as e:
    print('Sorry you need to enter an integer number ',e)
    
except:
    print("Something went wrong....",sys.exc_info()[0])
          
print("Ewery person should have around",tasksPerPerson, "tasks") 
