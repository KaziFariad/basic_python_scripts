def Leap_or_not(year):
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print(year, " is a Leap Year")
    else:
        print(year, " is not a Leap Year")


y = int(input("Enter a year:"))
Leap_or_not(y)
