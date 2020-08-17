# remove() - 제거하고자 하는 항목이 없으면 오류 발생
# discard() - 제거하고자 하는 항목이 없어도 오류 발생하지 않음
# pop() - 맨 마지막 항목 제거 

n = int(input()) #집합요소 수
s = set(map(int, input().split())) #집합
N = int(input()) # 메소드 수
for _ in range(N):
    a, *b = input().split()
    
    if a == 'pop':
        s.pop()
    if a == 'remove':
        s.remove(int(*b))
    if a == 'discard':
        s.discard(int(*b))

print(sum(s))

