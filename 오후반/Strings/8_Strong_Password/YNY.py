#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):

    special_characters = "!@#$%^&*()-+"

    count = 0
    if any(i.isdigit() for i in password) == False:
        count += 1
    if any(i.islower() for i in password) == False:
        count += 1
    if any(i.isupper() for i in password) == False:
        count += 1
    if any(i in special_characters for i in password) == False:
        count+=1
    return max(count,6-n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
