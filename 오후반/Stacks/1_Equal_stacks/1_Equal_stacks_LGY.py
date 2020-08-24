#!/bin/python3

import os
import sys

def equalStacks(h1, h2, h3):
    while(1):
        s1 = sum(h1)
        s2 = sum(h2)
        s3 = sum(h3)
        
        total = [s1,s2,s3]      
        Top = max(total)
        
        long_arr = total.index(Top)
        
        if  long_arr== 0:
            h1.pop(0)
        elif long_arr == 1:
            h2.pop(0)
        elif long_arr == 2:
            h3.pop(0)

        
        if s1 == s2 == s3 :
            ans = s1
            break

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split() # 각각의 블록 수

    n1 = int(n1N2N3[0]) # 5

    n2 = int(n1N2N3[1]) # 3

    n3 = int(n1N2N3[2]) # 4

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
