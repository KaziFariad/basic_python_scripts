#  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math


def LCM(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i // math.gcd(ans, i)
    return str(ans)


print(LCM(int(input("Enter a number: "))))
