# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

L = [input() for _ in range(N)]

print(len(set(L)))

