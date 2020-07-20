#!/bin/python3

import sys


N = int(input().strip())
if N % 2 !=0:
    print('Weird')
elif 2 <= N and N <= 5:
    print('Not Weird')
elif 6 <= N and N <= 20:
    print('Weird')
else:
    print('Not Weird')
