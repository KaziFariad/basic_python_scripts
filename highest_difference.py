def highest_difference(a, b, c):
    """
      This function helps in finding out the maximum difference between three numbers!
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return max(diff1, diff2, diff3)


print(highest_difference(1, 23, 44))
