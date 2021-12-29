import datetime
print("Week number of the year:", datetime.date.today().strftime("%W"))
print("Day in the week:", datetime.date.today().strftime("%w"))
print("Date:", datetime.date.today().strftime("%d"))
print("Month:", datetime.date.today().strftime("%B"))
print("Year:", datetime.date.today().strftime("%Y"))
print("Day in the year:", datetime.date.today().strftime("%j"))
print("Weekday:", datetime.date.today().strftime("%A"))
print("Timestamp:", datetime.datetime.now())
