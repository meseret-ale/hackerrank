"""
ANSWER
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding 
the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick
remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all
the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.

Example

The shortest stick length is , so cut that length from the longer two and discard the pieces of length . Now the lengths are 
. Again, the shortest stick is of length , so cut that amount from the longer stick and discard those pieces. There is only 
one stick left, , so discard that stick. The number of sticks at each iteration are .
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    
    result = []
    n = len(arr)
    s = Counter(arr)
    for i in sorted(s.keys()):
        result.append(n)
        n -= s[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
