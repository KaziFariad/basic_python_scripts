#  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#  Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    num = number
    rev = 0
    while(num != 0):
        tem = num % 10
        rev = rev*10+tem
        num = num//10
    if(rev == number):
        return True
    else:
        return False


def LargestPalindrome(num):
    prod = 1
    for i in range(10**num-1, 0, -1):
        for j in range(i, 0, -1):
            prod = i*j
            if(isPalindrome(prod)):
                return prod


print(LargestPalindrome(int(input("Enter a number: "))))
