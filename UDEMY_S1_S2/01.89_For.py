persons = ["Michal","Zdzislaw","Tomek","Zenek"]
domain = "gmail.com"

for person in persons:
    email = person + "@" + domain
    print("Email for\t",person, "\t\t is \t\t", email)

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
elements =[]

for d in data:
    elements = d.split(':') 
    
    print('')
    print(elements[0])
    print(elements[1])
