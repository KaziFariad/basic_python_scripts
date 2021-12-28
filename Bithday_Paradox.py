import datetime
import random
Bday = []
BirthDay = []
i = 0
while(i < 50):
    year = random.randint(1960, 2019)
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = True
    else:
        leap = False
    month = random.randint(1, 12)
    if(month == 2 and leap):
        day = random.randint(1, 29)
    elif(month == 2 and not leap):
        day = random.randint(1, 28)
    elif(month % 2 != 0 and month <= 7):
        day = random.randint(1, 31)
    elif(month % 2 == 0 and month > 7):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    date = datetime.date(year, month, day)
    day_of_year = date.timetuple().tm_yday
    Bday.append(day_of_year)
    BirthDay.append(date)
    i += 1
i = 0
count = 0
Bday.sort()
while(i < 50):
    print(Bday[i])
    if(Bday[i] == Bday[i-1] and i != 0):
        count += 1
    i += 1
print("There were ", count, "collisions!")
