import datetime

print('Minimum and maximum',datetime.MINYEAR, datetime.MAXYEAR)

d1 = datetime.timedelta(days=1,hours=2,minutes=30)
print(d1)
d2 = datetime.timedelta(days=-1,hours=2,minutes=-30)
print(d2)

print("timedelta sum = " ,d1+d2)

#date

print("Today is",datetime.date.today())
today = datetime.date.today()
print('\n')
daysToPay = datetime.timedelta(days=7)
print("Bill should be payed in" ,daysToPay.days ,"days")
print(today+daysToPay)

print("------------------------------------------")

endOfTheWorld =datetime.date.max
print("End of the world by python is:   ",endOfTheWorld,endOfTheWorld.weekday())

bornDate = datetime.date(1993,7,28)
print(today-bornDate)

#datetime

print("now\t",datetime.datetime.now())
print("today\t",datetime.datetime.today())
print("utcnow\t",datetime.datetime.utcnow())
print("weekday\t",datetime.datetime.now().weekday())

print("%a",datetime.datetime.now().strftime("%a"))

print("%A",datetime.datetime.now().strftime("%A"))
print("%w",datetime.datetime.now().strftime("%w"))
print("%Y-%m-%d-%H-%M-%S-%f",datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))


#LAB

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
import math
print(len(inputdata))
print(len(factortable))
i=0
if len(inputdata) == len(factortable):
    print('ok')
    for i in range(0,len(inputdata)):
        print(i,'\n')
        value = inputdata[i] - factortable[i] * inputdata[i]
        maxValue = inputdata[i] + factortable[i] * inputdata[i]
        i+=1
        print (value,"        ",maxValue)
else:
    print("inputdata and factortable need to have equal number of elements")

