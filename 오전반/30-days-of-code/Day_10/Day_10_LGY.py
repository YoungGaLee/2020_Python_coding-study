import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    Binary = format(n, 'b')
    count = 0
    ans_max = 0

    for i in Binary:
        if i == '1' : 
            count += 1
            if count > ans_max : ans_max = count
        
        else :
            count = 0 

    print(ans_max)
