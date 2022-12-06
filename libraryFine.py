"""
ANSWER
Your local library needs your help! Given the expected and actual return dates for a library book, create
a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 
or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be .
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
   
    if y1 == y2:
        if m1 == m2:
            if d2 > d1:
                return 0
            return 15 * abs(d1 - d2)
        else:
            if m2 > m1:
                return 0
            return 500 * abs(m1 - m2)
    elif y2 > y1:
        return 0
    else:
        return 10000
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
