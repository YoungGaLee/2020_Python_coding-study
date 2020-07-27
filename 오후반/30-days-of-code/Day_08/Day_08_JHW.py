# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
spl = []
dic={}
name=""
for i in range(t):
    spl.append(input().split())
    dic[spl[i][0]]=spl[i][1]
for j in range(t):
    name=str(input())
    if name in dic:
        print(name+"="+dic.get(name))
    else:
        print("Not found")
