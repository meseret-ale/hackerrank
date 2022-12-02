"""
ANSWER
Lily likes to play games with integers. She has created a new game where she determines the 
difference between a number and its reverse. For instance, given the number , its reverse is . 
Their difference is . The number  reversed is , and their difference is .

She decides to apply her game to decision making. She will look at a numbered range of days and will 
only go to a movie on a beautiful day.

Given a range of numbered days,  and a number , determine the number of days in the range that are beautiful. 
Beautiful numbers are defined as numbers where  is evenly divisible by . If a day's value is a beautiful number, 
it is a beautiful day. Return the number of beautiful days in the range.
"""
!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    stack = []
    for l in range(i, j+1):
        stack.append(l)
    revers = []
    for l in range(0, len(stack)):
        m = str(stack[l])
        ls = [i for i in m]
        ls.reverse()
        revers.append(int("".join(ls)))
    count = 0
    for i in range(0,len(stack)):
        ans = (abs(stack[i] - revers[i]))/k
        if ans % 1 == 0:
            count += 1
        ans = 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
