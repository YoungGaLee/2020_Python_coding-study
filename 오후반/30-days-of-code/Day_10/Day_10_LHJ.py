#!/bin/python3

import sys


n = str(bin(int(input().strip())))
n = n[2:]
n = [str(i) for i in n.split('0')]
print(len(max(n)))