"""
answer
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1, The elements of the first array are all factors of the integer being considered
2, The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    result = 0
    for i in range(max(a), min(b)+1):
        isFactorMultiple = True
        for l in a:
            if i % l != 0:
                isFactorMultiple = False
                break
        for l in b:
            if l % i != 0:
                isFactorMultiple = False
                break
        if isFactorMultiple == True:
            result += 1
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
