import sys


def day3(n):
    if (n % 2 != 0):
        return "Weird"
    else:
        if ((2 <= n) and (n <= 5)):
            return "Not Weird"
        elif (6 <= n) and (n <= 20):
            return "Weird"
        elif (n > 20):
            return "Not Weird"


n = int(input().strip())
result = day3(n)
print(result)