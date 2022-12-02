"""
ANSWER
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, 
they advertise it to exactly  people on social media.

On the first day, half of those  people (i.e., ) like the advertisement and each shares it with 
of their friends. At the beginning of the second day,  people receive the advertisement.

Each day,  of the recipients like the advertisement and will share it with  friends on the following day. 
Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day,
beginning with launch day as day .
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here

    liked = 0
    counter = 0
    shared = 5
    for i in range(1,n+1):
        liked = shared // 2
        shared = liked * 3
        counter += liked
    return counter 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
