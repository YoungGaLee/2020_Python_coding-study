n = int(input()) 

#s라는 집합을 만들어 숫자 요소들을 뛰어쓰기 기준으로 잘라서 int 형식으로 저장
s = set(map(int, input().split())) 

m = int(input())

for i in range(m): 
    S = input().split() #s에 뛰어쓰기 기준으로 잘라서 저장
    if S[0] == 'pop' : 
        s.pop()

    elif S[0] == 'remove':
        s.remove(int(S[1]))
    
    elif S[0] == 'discard':
        s.discard(int(S[1]))

print(sum(s))
