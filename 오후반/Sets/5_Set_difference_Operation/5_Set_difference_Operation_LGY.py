# Enter your code here. Read input from STDIN. Print output to STDOUT
E_n = int(input())
E = set(input().split())
F_n = int(input())
F = set(input().split())

print(len(E.difference(F)))
