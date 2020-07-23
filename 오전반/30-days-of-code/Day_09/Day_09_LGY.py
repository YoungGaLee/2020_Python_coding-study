#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
#def factorial(n):

#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #result = factorial(n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    
    
def factorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * factorial(n - 1) 
 
 
 
 
n = int(input()) 
print(factorial(n)) 

#다시
