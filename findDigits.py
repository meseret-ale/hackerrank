"""
ANSWER
An integer  is a divisor of an integer  if the remainder of .

Given an integer, for each digit that makes up the integer determine whether it is a divisor.
Count the number of divisors occurring within the integer.

Example

Check whether ,  and  are divisors of . All 3 numbers divide evenly into  so return .


Check whether , , and  are divisors of . All 3 numbers divide evenly into  so return .


Check whether  and  are divisors of .  is, but  is not. Return .

Function Description

Complete the findDigits function in the editor below.

findDigits has the following parameter(s):

int n: the value to analyze
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    count = 0
    s = [int(i) for i in str(n)]
    for i in range(0,len(s)):
        if s[i] == 0:
            continue
        else:
            if n % s[i] == 0:
                count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
