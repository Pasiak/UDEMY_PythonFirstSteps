# playing with time

import time

print("Current time is ... unix epoch", time.time())
print("\n")
print("Current time is ... tuple", time.localtime(time.time()))
print("\n")
print("Current time is ... for human", time.asctime(time.localtime(time.time())))
print("\n")
print("Current time is ... for human", time.localtime(time.perf_counter()))

print("\n")
# calendar

import calendar
print('-----------------------------------------')
print(calendar.month(2017,9,w=5,l=2))
print('-----------------------------------------')
print(calendar.month(2017,9))
print('-----------------------------------------')
print(calendar.weekday(2017,9,29))
print('-----------------------------------------')
calendar.setfirstweekday(6)
print('-----------------------------------------')
print(calendar.month(2017,9))
print('-----------------------------------------')
print('is 2020 a leap year?',calendar.isleap(2020))

print('-----------------------------------------')
print('Leap days 00-17',calendar.leapdays(2000,2017))
print('Leap days 00-20',calendar.leapdays(2000,2020))    #2020 nie jest brane po uwage
print('Leap days 00-21',calendar.leapdays(2000,2021))

print(calendar.calendar(2019))


#LAB

print(calendar.month(1993,7))
