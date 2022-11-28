"""
answer
There is a large pile of socks that must be paired by color. Given an array of integers
representing the color of each sock, determine how many pairs of socks with matching 
colors there are.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    stack = []
    list1 = []
    for i in range(0, len(ar)):
        ls = []
        ls.append(ar[i])
        if ar[i] in list1:
            continue
        else:
            for j in range(i+1, len(ar)):
                if ar[i] == ar[j]:
                    ls.append(ar[i])
        if len(ls) > 1:
            list1.append(ar[i])
            stack.append(ls)

    count = 0
    for i in range(0, len(stack)):
        length = len(stack[i])
        while length >= 2:
            if length >= 2:
                count += 1
            length -= 2
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
