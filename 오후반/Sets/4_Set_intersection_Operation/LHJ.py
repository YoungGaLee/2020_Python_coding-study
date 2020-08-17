n_1 = int(input())
set_1 = set(map(int, input().split()))

n_2 = int(input())
set_2 = set(map(int, input().split()))

res = set_1.intersection(set_2)
print(len(res))
