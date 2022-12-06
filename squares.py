"""
ANSWER
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, 
inclusive of the endpoints. Sherlock must determine the number of square integers within that range.

Note: A square integer is an integer which is the square of an integer, e.g. .

Example


There are three square integers in the range:  and . Return .

Function Description

Complete the squares function in the editor below. It should return an integer representing the number of square integers 
in the inclusive range from  to .

squares has the following parameter(s):

int a: the lower range boundary
int b: the upper range boundary
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    
    count = 0
    sqr = 0
    for i in range(a,b+1):
        if math.sqrt(i) % 1 == 0:
            count += 1
            sqr = math.sqrt(i)+1
            break
    if sqr == 0:
        return 0
    while b >= sqr*sqr:
        count += 1
        sqr += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
