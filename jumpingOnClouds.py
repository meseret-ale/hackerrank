"""
ANSWER
A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can 
be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds,  and an energy level . The character starts from  and uses  unit of energy to make a 
jump of size  to cloud . If it lands on a thundercloud, , its energy () decreases by  additional units. The game ends
when the character lands back on cloud .

Given the values of , , and the configuration of the clouds as an array , determine the final value of  after the game
ends.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    stack = []
    ms = 0
    while True:
        if (ms + k) % len(c) == 0:
            stack.append(0)
            break
        else:
            stack.append((ms + k) % len(c))
            ms = (ms + k) % len(c)
            
    for i in range(0,len(stack)):
        if c[stack[i]] == 1:
            e -= 3
        else:
            e -=1
            
    return e
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
