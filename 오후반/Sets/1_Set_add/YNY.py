# Enter your code here. Read input from STDIN. Print output to STDOUT
a=[]
num = int(input().strip())
for i in range(num):
    data=input()
    a.append(data)
a = set(a)
print(len(a))
