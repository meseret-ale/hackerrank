"""
answer
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle.
In this PDF viewer, each word is highlighted independently. For example:

PDF-highighting.png

There is a list of  character heights aligned by index to their letters. For example, 
'a' is at index  and 'z' is at index . There will also be a string. Using the letter heights given, 
determine the area of the rectangle highlight in  assuming all letters are  wide.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    alphbet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dic = {}
    for i in range(0, len(alphbet)):
        dic[alphbet[i]] = h[i]
    maxs = 0
    for i in range(0,len(word)):
        maxs = max(maxs,dic[word[i]])
    
    return maxs * len(word)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
