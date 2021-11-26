def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


num = int(input())
for x in range(2, num):
    if (prime(x)):
        print(x, end=" ")
