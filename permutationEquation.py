"""
ANSWER
Given a sequence of  integers,  where each element is distinct and satisfies . 
For each  where , that is  increments from  to , find any integer  such that  and keep a 
history of the values of  in a return array.

Example


Each value of  between  and , the length of the sequence, is analyzed as follows:
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    
    first = []
    for i in range(1, len(p)+1):
        m = 0
        while True:
            if i == p[m]:
                first.append(m + 1)
                break
            m += 1
    s = []
    for j in range(0,len(p)):
        for i in range(0, len(p)):
            if first[j] == p[i]:
                s.append(i+1)
                break
                
    mm = 1
    for i in range(0,len(first)):
        if mm != p[first[i]-1]:
            s.remove(i)
        mm += 1
            
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
