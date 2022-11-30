"""
answer
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example


There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    stack = []
    a.sort()
    first = a[0]
    ls = []
    ls.append(a[0])
    for i in range(1,len(a)):
        
        if a[i] - first <= 1:
            ls.append(a[i])
        else:
            stack.append(ls)
            ls = []
            ls.append(a[i])
            first = a[i]
    stack.append(ls)
    maxs = 0
    for i in range(0, len(stack)):
        maxs = max(maxs,len(stack[i]))
    return maxs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
