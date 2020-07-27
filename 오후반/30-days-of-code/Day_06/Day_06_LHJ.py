n=int(input())
s=[]
p=0

for i in range(n):
    s=input()
    for k in range(0,len(s)):
        if k%2==0:
            print(s[k],end='')
    print(end=' ')
    for j in range(0,len(s)):
        if j%2!=0:
            print(s[j],end='')
        if j == len(s)-1:
            print('')