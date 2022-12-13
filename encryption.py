"""
ANSWER
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

Example


After removing spaces, the string is  characters long.  is between  and , so it is written in the form of a grid with 7 rows and 8 columns.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    
    n = math.sqrt(len(s))
    foot = int(n-(n%1))
    ceil = foot + 1
    colomen = ceil
    row = 0
    if n % 1 == 0:
        colomen = foot
    else:
        if foot * ceil < len(s):
            row = ceil
        else:
            row = foot
    lsi = []
    for i in range(0,colomen):
        ls = []
        for j in range(i,len(s),colomen):
            ls.append(s[j])
        lsi.append("".join(ls))

    return " ".join(lsi)
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
