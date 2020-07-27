#!/bin/python3

import sys

def factorial(n):
    a = n
    while n != 1 :
        a *= (n-1)
        n -= 1
    return a

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
