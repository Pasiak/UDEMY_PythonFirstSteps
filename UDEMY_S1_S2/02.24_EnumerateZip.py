workDays = [19, 21, 22, 21, 20, 22]

print(workDays)
print(workDays[2])

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)

for pos, value in enumeratedDays:
    print("Position ", pos, "value", value)

months = ["I", "II", "III", "IV", "V", "VI"]

monthsDays = list(zip(months, workDays))
print(monthsDays)

for m, d in monthsDays:
    print("month", m, "days", d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print("Position", pos, "month", m, "days", d)

# LAB

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for pos,(p, d, l) in enumerate(zip(projects, dates, leaders)):
    print(pos+1," The leader of", p, "started", d, "is", l)
