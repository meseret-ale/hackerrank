"""
ANSWER
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , 
find and print the number of letter a's in the first  letters of the infinite string.

Example


The substring we consider is , the first  characters of the infinite string. There are  occurrences 
of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    if len(s) >= n:
        count = 0
        for i in range(0,n):
            if s[i] == "a":
                count += 1
        return count
    
    else:
        count = 0
        for i in range(0,len(s)):
            if s[i] == "a":
                count += 1
        
        result = count * ((n-(n % len(s)))//len(s))
        for i in range(0,(n%len(s))):
            if s[i] == "a":
                result += 1
        return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
