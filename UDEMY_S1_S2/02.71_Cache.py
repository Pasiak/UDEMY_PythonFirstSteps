import time
import functools

@functools.lru_cache()
def Factorial(n):
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


start = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()

print("Execution time", stop - start)
print(Factorial.cache_info())


#LAB

a = 36

def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()
for i in range(1,a):
    print("{} = {}".format(i,fib(i)))
stop = time.time()
print("Execution time without cache", stop - start)
print("\n")
print("*"*40)

@functools.lru_cache()
def fibcache(n):
    if n <= 2:
        result = n
    else:
        result = fibcache(n - 1) + fibcache(n - 2)

    return result

start = time.time()
for i in range(1,a):
    print("{} = {}".format(i,fibcache(i)))
stop = time.time()
print("Execution time with cache", stop - start)
print(fibcache.cache_info())