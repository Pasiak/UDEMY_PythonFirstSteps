def GoFoward(*args):
    print("Going foward with",*args)

def GoBack(*args):
    print("Going back with",*args)

def Stop(*args):
    print("Stoping with",*args)

instructions = [GoBack,Stop,GoFoward]

dish = "Pizza"
for instr in instructions:
    instr(dish)

#LAB

def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

x = 8
tmp_return_value = x
transformations = [double,root,div2,negative]

for trans in transformations:
    tmp_return_value = trans(tmp_return_value)
    print(tmp_return_value)

