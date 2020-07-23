#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin_n=str(bin(n))
    bin_n=str(bin_n[2:])
    SepOnes=[]

    for i in bin_n.split('0'):
        SepOnes.append(i)

    MaxOnes=len(max(SepOnes))
    print(MaxOnes)
