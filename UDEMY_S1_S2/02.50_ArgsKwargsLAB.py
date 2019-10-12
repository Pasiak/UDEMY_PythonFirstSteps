def calculate_paint(efficency_ltr_per_m2, *fields):
    paintNeeded = 0
    for field in fields:
        paintNeeded += efficency_ltr_per_m2 * field
    return paintNeeded
    '''total_area = sum(fields)
    paint = total_area * efficency_ltr_per_m2
    return paint'''

wallAreas = [20,55,34,67,89,77]
print(calculate_paint(14,20,45,35,65,))
print(calculate_paint(14,*wallAreas))

#lab2
import os
def log_it(*args):
    path = r"C:\Users\El Patrico\Desktop\tempTXT\02.50_ArgsKwargsLab.txt"
    with open (path,'a') as file:
        for arg in args:
            line = (str(arg)+" ")
            file.write(line)

        file.write('\n')

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')