def getDigit(n):
    l = []
    while (n >= 10):
        val = n % 10
        l.insert(0, val)
        n = n // 10
    l.insert(0, n)
    print(l)
    return l


def dig_pow(n, p):

    # your code
    num_list = getDigit(n)
    print(num_list)
    cal = 0
    for i in range(0, len(num_list)):
        cal += pow(num_list[i], p)
        p += 1
    print(cal)
    if (pow(cal, 1, n) == 0):
        return (cal//n)
    return -1


print(dig_pow(46288, 3))
