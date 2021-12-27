given_time = input("Enter the time in 24hrs format:\n")

list_time_values = list(map(int, given_time.split(":")))

am = True

if (list_time_values[0]) > 12:
    list_time_values[0] -= 12
    list_time_values[0] = str(list_time_values[0]).zfill(2)
    am = False

for x in range(len(list_time_values)-1):
    print(list_time_values[x], end=":")
print(list_time_values[len(list_time_values)-1], end="")
if am:
    print(" AM")
else:
    print(" PM")
