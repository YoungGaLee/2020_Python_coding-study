#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    ans = ''
    space = 0

    for i in range(len(s)):
        if s[i]==' ': #빈칸이면 빈칸넣기
            space = 1 #빈칸이 있다고 말하기
            ans+=s[i]
        elif i==0 or (space>0 and s[i]!=' '):
            ans += s[i].capitalize()
            space = 0           
        else:
            ans += s[i]
    return ans





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
