def double(x):
    return x * 2


x = 10
print(double(10))

# Same with Lambda

x = 10
f = lambda x: x * 2
print(f(x))


# With two args
def power(x, y):
    return x ** y


x = 3
y = 5
print(power(x, y))
# lambda
f = lambda x, y: x ** y
print(f(x, y))

# Lists

list_numbers = [2, 4, 6, 9, 15, 34, 22]


def is_odd(x):
    return x % 2 != 0


print(is_odd(7))

filteredList = list(filter(is_odd, list_numbers))
print(filteredList)

# shorter!
print(list(filter(lambda x: x % 2 != 0, list_numbers)))


def generate_multiply_function(n):
    return lambda x: n * x


mul2 = generate_multiply_function(2)
print(mul2(10))

#LAB
text_list = ['x','xxx','xxxxx','xxxxxxx','']


print(list(map(lambda s:len(s),text_list)))
