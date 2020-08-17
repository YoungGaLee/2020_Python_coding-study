#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    x = s.split(" ") 
    #한개 뛰어쓰기 기준으로 나눈다.(test 케이스 중에 뛰어쓰기 두개가 있음)
    count = []

    for i in x:
        s = i[:1].upper() + i[1:]
        count.append(s)
    result = (' ').join(count)
        
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
