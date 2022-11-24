"""Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max1 = scores[0]
    min1 = scores[0]
    sums1 = 0
    sums2 = 0
    stack = []
    for i in range(1, len(scores)):
        
        if scores[i] > max1:
            sums1 += 1
        elif scores[i] < min1:
            sums2 += 1
            
        max1 = max(max1, scores[i])
        min1 = min(min1, scores[i])
    stack.append(sums1)
    stack.append(sums2)
    return stack

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
