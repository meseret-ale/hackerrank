"""
ANSWER
The factorial of the integer , written , is defined as:

Calculate and print the factorial of a given integer.

For example, if , we calculate  and get .

Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):

n: an integer
Note: Factorials of  can't be stored even in a  long long variable. Big integers must be used for such calculations. 
Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to 
handle huge values.

We recommend solving this challenge using BigIntegers.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    mult = 1
    for i in range(n,0,-1):
        mult *= i
    print(mult) 
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
