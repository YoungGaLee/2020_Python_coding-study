import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    '''


    for i in range(n):
        print(arr[n-1-i], end=" ")
    
    '''

    arr.reverse()
