import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    Binary = format(n, 'b')
    total = []
    count = 0

    for i in Binary:
        if i == '1' : 
            count += 1
        
        else :
            total.append(count)
            count = 0 

        total.append(count)
        
    print(max(total))
