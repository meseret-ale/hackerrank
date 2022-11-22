"""
HackerLand University has the following grading policy:

1    Every student receives a grade in the inclusive range from 0 to 100.
2    Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

1   If the difference between the grade and the next multiple of 5 is less than 3, round 5 up to the next multiple of .
2   If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    stack = []
    m = None
    for i in range(0, len(grades)):
        m = None
        if grades[i] < 35:
            stack.append(grades[i])
        else:
            m = str(grades[i])
            s = m[1]
            if int(s) == 5:
                stack.append(grades[i])
            elif int(s) == 0:
                stack.append(grades[i])
            
            elif int(s) < 5:
                if 5 - int(s) < 3:
                    stack.append(grades[i] + 5 - int(s))
                else:
                    stack.append(grades[i])
                            
            elif int(s) > 5:
                if 10 - int(s) < 3:
                    stack.append(grades[i] + 10 - int(s))
                else:
                    stack.append(grades[i])
                
    return stack     
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
