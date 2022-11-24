
"""Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
Using the information given below, 
determine the number of apples and oranges that land on Sam's house."""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    stack = []
    sums = 0
    for i in range(0,len(apples)):
        count = 0
        count = apples[i] + a
        if (count >= s) & (count <= t):
            sums += 1
            
    sums1 = 0
    for i in range(0,len(oranges)):
        count = 0
        count = oranges[i] + b
        if (count >= s) & (count <= t):
            sums1 += 1

    print(sums)
    print(sums1)
            
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
