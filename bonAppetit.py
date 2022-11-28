"""
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay 
for the items they consume. Brian gets the check and calculates Anna's portion. You must determine 
if his calculation is correct.

For example, assume the bill has the following prices: . Anna declines to eat item  which costs bill = [2,4,6].
If Brian calculates the bill correctly, Anna will pay k = bill[2]. If he includes the cost of 6, he will calculate (2 + 4) / 2. 
In the second case, bill[2] he should refund (2 + 4 + 6)/2 = 6 to Anna.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    count = 0
    for i in range(0, len(bill)):
        if i == k:
            continue
        count += bill[i]
        
    num = count // 2
    if num == b:
        print("Bon Appetit") 
    else:
        print(b - num) 
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
