#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    password = set(password)
    cnt = [0]*4
    for c in password:
        if c.isdigit():
            cnt[0] = 1
        elif c.islower():
            cnt[1] = 1
        elif c.isupper():
            cnt[2] =1
        else :
            cnt[3] = 1
        if sum(cnt) ==4:
            break
    return max(4 -sum(cnt), 6-n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
