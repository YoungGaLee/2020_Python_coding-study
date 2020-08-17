n_1 = int(input())
set_1 = set(input().split())

n_2 = int(input())
set_2 = set(input().split())

res = set_1 - set_2
print(len(res))
