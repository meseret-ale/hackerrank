"""
ANSWER
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and
others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud
plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting 
postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example

Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds
at indices  and . They could follow these two paths:  or . The first path takes  jumps while the second takes 
. Return .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    n = 0
    count = 0
    while True:
        if (n+2) > (len(c)-1):
            if (n+1) == (len(c)-1):
                return count + 1
            return count
                
        elif c[n+2] == 1:
            n += 1
            count += 1
        else:
            n += 2
            count += 1
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
