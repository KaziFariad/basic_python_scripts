#!/bin/python3

import math
import os
import random
import re
import sys


def calc(arr):
    pcount = 0
    ncount = 0
    zeros = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] > 0:
            pcount += 1
        elif arr[i] < 0:
            ncount += 1
    print("{:.6f}".format(pcount/len(arr)))
    print(round(ncount/len(arr), 6))
    print("{:.6f}".format(zeros/len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    calc(arr)
