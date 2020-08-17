num_1 = int(input())
A = set(map(int,input().split()))#뛰어쓰기 기준으로 나눠서 집합으로 저장
num_2 = int(input())
B = set(map(int,input().split()))

result = len(A.difference(B))
print(result)
