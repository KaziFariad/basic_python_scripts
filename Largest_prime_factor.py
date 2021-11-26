# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = int(input("Enter a number: "))
max = 1
while(num % 2 == 0):
    num /= 2
    max = 2

for i in range(3, int(num**0.5), 2):
    while(num % i == 0):
        num /= i
        max = i

if(num > 2):
    max = num

print(max)
