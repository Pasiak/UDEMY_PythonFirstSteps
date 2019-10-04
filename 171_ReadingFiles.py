##file = open(r"C:\Users\El Patrico\Desktop\text.txt","r")
##content = file.read()
##print(content)
##file.close()
##
##print("-----------------------------------------------------")
##
##with open(r"C:\Users\El Patrico\Desktop\text.txt","r") as file:
##    content = file.read()
##    print(content)
##
##print("-----------------------------------------------------")
##
##with open(r"C:\Users\El Patrico\Desktop\text.txt","r") as file:
##    for line in file:
##        print(line)
##print("-----------------------------------------------------")
##
##file = open(r"C:\Users\El Patrico\Desktop\text.txt","r")
##fragment = file.read(10)
##while fragment:
##    print(file.tell(),fragment)
##    fragment = file.read(10)
##file.close()
##
##LAB
##file_path = r"C:\Users\El Patrico\Desktop\aptekiLAB.txt"
##with open(file_path,"r") as file:
##    for line in file:
##        line = line.replace('\n','')
##        order = line.split(",")
##        if len(order) == 3:
##            print('Order from drugstore "%s", item "%s", amount %s' % (order[0],order[1],order[2]))
##        else:
##            print("\n Line %s malformed!!!" % line,"\n")
##            
##print("Processing finished")
        
#LAB2 TRY and Except

import sys
file_path = r'C:\Users\El Patrico\Desktop\aptekiLAB.txt'
amount = 1
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
            
        except ValueError as e:
            print("\nData conversion failed in line:\n",line,"\nError code :",e,"\n")

        except IndexError as e:
            print("\n Out of index error in line:\n",line,"\nError code :",e,"\n")
        
            
        
        except:
            print("\nProblem with line %s" % line)
            print(sys.exc_info()[0],sys.exc_info()[1])
            print('\n')
            
print("Processing finished")
