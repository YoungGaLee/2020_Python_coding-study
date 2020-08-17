n = int(input()) # stamp 개수를 변수 n에 저장
s = set() #s라는 집합만들기
for i in range(n): #for 이용해서 stamp 나라 하나씩
    s.add(input()) #stamp를 집합 s에 추가    
print(len(s)) #집합 s 길이 출력
