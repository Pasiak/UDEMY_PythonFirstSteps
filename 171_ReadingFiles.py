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

#LAB
file_path = r"C:\Users\El Patrico\Desktop\text.txt"
with open(file_path,"r") as file:
    for line in file:
        line = line.replace('\n','')
        order = line.split(",")
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0],order[1],order[2]))
        else:
            print("Line %s malformed!!!" % line)
print("Processing finished")
        
