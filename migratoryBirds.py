"""
Answer
Given an array of bird sightings where every element represents a bird type id, determine the id of the most
frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their 
ids.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    l = [0] * len(arr)
    for i in range(len(arr)):
        l[arr[i]] += 1
    return l.index(max(l))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
