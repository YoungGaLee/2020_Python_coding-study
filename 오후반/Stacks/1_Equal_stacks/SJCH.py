#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    min_sum = min(sum1, sum2, sum3)
    
    while sum1 > min_sum or sum2 > min_sum or sum3 > min_sum :
        while sum1 > min_sum:
            sum1 -= h1.pop(0)
        while sum2 > min_sum:
            sum2 -= h2.pop(0)
        while sum3 > min_sum:
            sum3 -= h3.pop(0)
        min_sum = min(sum1, sum2, sum3)
    return min_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
