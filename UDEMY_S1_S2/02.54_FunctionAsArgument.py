def Bake(what):
    print("Baking {}".format(what))


def Add(what):
    print("Adding {}".format(what))


def Mix(what):
    print("Mixing {}".format(what))


cookbook = [(Add, "milk"), (Add, 'eggs'), (Add, 'flour'), (Mix, 'ingredients'), (Bake, 'cookies')]

for activity,object in cookbook:
    activity(object)

print('-'*30)

def Cook(activity,object):
    activity(object)

#LAB
def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

def generate_values (activity,x_table):
    results = []
    for x in x_table:
        results.append(activity(x))
    return results



x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))
