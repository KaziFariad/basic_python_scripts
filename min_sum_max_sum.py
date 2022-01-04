import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    arr.sort()
    max_sum = 0
    min_sum = 0
    for i in range(0, len(arr)):
        if(i != len(arr)-1):
            min_sum += arr[i]
        if(i != 0):
            max_sum += arr[i]
    print("Maximum is:", max_sum, "\nMinimum is:", min_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
