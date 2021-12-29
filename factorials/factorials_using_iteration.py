def factorial(n):
    f = 1
    if(n == 0 or n == 1):
        return 1
    for i in range(2, n+1):
        f = f*i
    return f


print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
