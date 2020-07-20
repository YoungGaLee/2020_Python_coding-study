import sys


def my_func(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


n = int(input().strip())
result = my_func(n)
