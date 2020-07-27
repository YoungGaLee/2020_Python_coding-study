import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())                        # 13
    binary_n = bin(n)[2:]                   # '0b1101' --> '1101'
    list_sequence_1 = binary_n.split('0')   # ['11', '1']
    print(len(max(list_sequence_1)))