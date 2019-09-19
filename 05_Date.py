print("Hello what day is today?")
from datetime import date
print("Today is")
print (date.today().strftime("%A"))

#  Komentarze


'''

   Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakladamy ze:
-liczba mrugniec na minute to 20
-liczba minut w godzinie to 60
-liczba godzin w dobie 24
-liczba lat (czyli nasz X) 50
Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
powinna wynosic 16

'''

# l mrugnięć na min
blinksPerMin = 20
# l minut w godzinie i godzin w dobie

minInHour = 60
hoursInDay = 16
daysInYears = 365

# Liczba lat

years = 50


print (blinksPerMin * minInHour * hoursInDay * daysInYears)

#definitionOfVariables
daysOfWorkPermonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print((daysOfWorkPermonth * monthsInYear - vacation)*yearsOfWOrk)


input ("Press Enter to continue")
