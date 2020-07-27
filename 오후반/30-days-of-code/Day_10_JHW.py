#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b=str(format(n,'b'))
    result=1
    c=len(b)
    b=b+'0'
    mylist = [0]*100
    j=0
    for i in range(c):
        if b[i]=='1' and b[i+1]=='1':
            result+=1
        if b[i+1]=='0':
            mylist[j]=result
            result=1
            j+=1
    print(max(mylist))
