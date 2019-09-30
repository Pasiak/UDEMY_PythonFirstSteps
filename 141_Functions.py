


def PrintHello():
    #Print hello
    print("Hello")
    return

#LAB

def PrintCat():
    txt = r'''
|\---/|
| o_o |
 \_^_/'''
    print(txt)
    return
    
def PrintBear():
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    print(txt)
    return
    
def PrintBat():
    txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       '''
    print(txt)
    return

def PrintAnimal(*animal):

    for element in animal:
        if element == 'cat':
            PrintCat()
    ##        isPrinted = True
    ##        return isPrinted
        elif element == 'bat':
            PrintBat()
    ##        isPrinted = True
    ##        return isPrinted
        elif element == 'bear':
            PrintBear()
    ##        isPrinted = True
    ##        return isPrinted
        else:
            print("Please type: cat, bat, or bear to get ASCIIArt")
    ##        isPrinted = False
    ##        return isPrinted


