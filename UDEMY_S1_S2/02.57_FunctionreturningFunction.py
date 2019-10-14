def CreateFunction(kind="+"):
    source = '''
def f(*args):
    result = 0
    for a in args:
        result {}=a
    return result    
'''.format(kind)
    exec(source, globals())
    return f


f_add = CreateFunction('+')
print(f_add(2, 3, 4, 5, 6))

#LAB
from datetime import datetime

def FunctionGenerate(time=3600):

    source = '''
def f(date1,date2):
    delta = date2 - date1
    delta_in_sec = delta.total_seconds()
    print('Time in sec: ',delta_in_sec)
    return divmod(delta_in_sec,{})[0]
    '''.format(time)
    exec(source,globals())
    return f

time_span_m = FunctionGenerate(60)
time_span_h = FunctionGenerate(3600)
time_span_d = FunctionGenerate(86400)

start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()
print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))

