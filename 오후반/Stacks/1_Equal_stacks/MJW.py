#!/bin/python3

import os

def equalStacks(h1, h2, h3):
    h_list = [h1, h2, h3]
    sum_h = [sum(h1), sum(h2), sum(h3)]

    while len(set(sum_h)) != 1:
        min_h = min(sum_h)

        for i in range(3):
            if sum_h[i] > min_h:
                x = h_list[i].pop(0)
                sum_h[i] -= x

    return sum_h[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
