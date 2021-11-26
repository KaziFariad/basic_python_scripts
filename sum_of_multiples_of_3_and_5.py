def Multiples_of_3_and_5(num):
    l = []
    for i in range(1, num):
        if (i % 3 == 0 or i % 5 == 0):
            l.append(i)
    return l


def Sum_of_Multiples(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]

    return sum


print(Sum_of_Multiples(Multiples_of_3_and_5(int(input("Enter a number: ")))))
