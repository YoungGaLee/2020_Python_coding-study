#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    new_list=""
    for i in range(0,n):
        new_list+=str(arr[i])
        new_list+=" "
    print(new_list)
