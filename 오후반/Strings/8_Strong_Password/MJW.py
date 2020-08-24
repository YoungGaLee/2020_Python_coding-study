#!/bin/python3

import os


def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    add = 0

    if len(set(password) & set(numbers)) == 0:
        add += 1
    if len(set(password) & set(lower_case)) == 0:
        add += 1
    if len(set(password) & set(upper_case)) == 0:
        add += 1
    if len(set(password) & set(special_characters)) == 0:
        add += 1

    if len(password) + add < 6:
        add += (6 - (len(password) + add))

    return add


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
