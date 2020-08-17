num_1 = int(input())
A = set(input().split())#뛰어쓰기 기준으로 나눠서 집합으로 저장
num_2 = int(input())
B = set(input().split())

result = A.intersection(B) #intersection으로 교집합해줌
print(len(result))
