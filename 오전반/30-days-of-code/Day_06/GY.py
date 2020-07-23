# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for _ in range(N):
    n = "" # 홀
    nn = ""  # 짝
    P = input()
    for i in range(len(P)):
        if i % 2 == 1 : # 홀수일때
            n += P[i]
        else :
            nn += P[i] 
        
    print(nn , n)
