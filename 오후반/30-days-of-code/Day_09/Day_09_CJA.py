import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
        # n이 1이하일 경우 1을 출력한다.
    else:
        return n * factorial(n - 1)
        # n이 1보다 클 경우 n!의 값을 출력한다.



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')
