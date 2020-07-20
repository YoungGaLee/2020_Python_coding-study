#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    i=0
    result=0
    while i<10:
        i=i+1
        result=n*i
        print("%d x %d = %d" %(n, i, result))
