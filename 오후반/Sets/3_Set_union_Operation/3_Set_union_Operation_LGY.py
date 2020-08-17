first = int(input())
A = set(input().split())

second = int(input())
B = set(input().split())

result = A.union(B) 
print(len(result))
