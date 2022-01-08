#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(1, n+1):
        for j in range(n):
            if(i+j < n):
                print(" ", end="")
            else:
                print("#", end="")
        print()


if __name__ == '__main__':
    n = int(input())

    staircase(n)
