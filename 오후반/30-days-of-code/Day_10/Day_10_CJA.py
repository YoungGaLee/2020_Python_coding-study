import math
import os
import random
import re
import sys


if __name__ == '__main__':
    
    n = int(input().strip())

    binary = bin(n)[2:]#이진수 변환
    one = binary.replace('0', ' ')
    arr= one.split()
    max_arr = max(arr)
    print(len(max_arr))
