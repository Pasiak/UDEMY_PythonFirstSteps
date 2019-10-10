def WeekDayInPolish(dayNumber):

    names = {
        0:"Poniedziałek",
        1:"Wtorek",
        2:"Środa",
        3:"CZwartek",
        4:"Piątek",
        5:"Sobota",
        6:"Niedziela",
    }

    return names.get(dayNumber,"error")
##print(WeekDayInPolish(12))


#LAB


import math
def GiveGeomSeqElement(a1=2,factor=2,index=2):
    value = a1*pow(factor,index-1)
    return value
print('2^64 =',GiveGeomSeqElement(1,2,64))

def GiveGeomSeqElement2(a1=3,factor=2,maxindex=10):
    for i in range(0,maxindex):
        value = a1*pow(factor,i)
        print(i,"    ",value)
GiveGeomSeqElement2()
GiveGeomSeqElement2(3,4,4)
