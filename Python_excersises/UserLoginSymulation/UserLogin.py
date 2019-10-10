import random


def generateRandomPassword(passwordLenght):
    if passwordLenght < 8:
        print("Your generate password need to be longer than 8 digits. Plase input value higher that 8")
        input(passwordLenght)
    ints = range(33, 127)
    password: str = ""

    for i in range(passwordLenght):
        password += chr(random.choice(ints))
    print("Your password is: ",password)
    return password

