#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    res_s = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ': 
            res_s += s[i].upper()
            continue
        res_s += s[i]
    return res_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
