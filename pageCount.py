"""
answer
A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the
book. They always turn pages one at a time. When they open the book, page  is always on the right side:

image

When they flip page , they see pages  and . Each page except the last page will always be printed on both sides. The last page may
only be printed on the front, given the length of the book. If the book is  pages long, and a student wants to turn to page , 
what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    
    right = 1
    counter1 = 0
    while right < p:
        right += 2
        counter1 += 1
    if n % 2 == 0:
        left = n
    else:
        left = n - 1
    counter2 = 0
    while left > p:
        left -= 2
        counter2 += 1
    if counter1 > counter2:
        return counter2 
    return counter1
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
