def DoAction (action, parameter):
    print("action",action)
    print("parameter:",parameter)
    return

DoAction('buy','shoes')
    
def DoAction2 (action, *parameter):
    print("action",action)
    print("parameter:",parameter)
    
    for element in parameter:
        print("element ",element)
    return

DoAction2('buy','shoes','socks','T-shirt')

def DoAction3 (action, what, **parameter):
    print("action",action)
    print("what",what)
    print("parameter:",parameter)
    
    for element in parameter:
        print(element,"=",parameter[element])
    return

DoAction3('buy','shoes',size=45,color='black',type="sport")


#LAB


