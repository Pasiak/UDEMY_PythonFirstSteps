import os
import math
import time

filesPath = [r'C:\Users\El Patrico\Desktop\tempTXT\02.40a',
             r'C:\Users\El Patrico\Desktop\tempTXT\02.40b']

for filePath in filesPath:
    with open(filePath, 'r') as file:
        print("File name :", os.path.basename(filePath))
        source = file.read()
        exec(source)


formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)
    i += 1
'''
for formula in formulas_list:

    resultLists = []
    print(formula)
    start = time.time()
    for x in argument_list:
        resultLists.append(exec(formula))
    stop = time.time()
    totalTime = stop - start
    print("Time :", totalTime)
    print('min = {}  max = {}'.format(min(resultLists), max(resultLists)))

for formula in formulas_list:

    resultLists = []
    print(formula)
    sourceCompiled = compile(formula, "intern path", "exec")
    startCompiled = time.time()
    for x in argument_list:
        resultLists.append(exec(sourceCompiled))

    stopCompiled = time.time()
    totalTimeCompiled = stopCompiled - startCompiled
    print("Time :", totalTimeCompiled)
    print('min = {}  max = {}'.format(min(resultLists), max(resultLists)))
'''

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()

    print("Calculation time: {}".format(stop - start))