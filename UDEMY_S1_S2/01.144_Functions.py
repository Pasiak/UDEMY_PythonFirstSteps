from datetime import date
from datetime import timedelta

def GiveWorkingDay(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):   # IF i set day as 1, it will be default 
    #Print the next working day
    
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    
    return workingday
print("Next working day is ",GiveWorkingDay())

def DaysToEndOfYear(*dates):
    
    for date_today in dates:
        
        

        CurrentYear = date_today.year
        
        NewYearEve = date(CurrentYear,12,31)
        DaysToNYE = NewYearEve - date_today
        print("Date",date_today,"days to end of year",DaysToNYE.days)
        

