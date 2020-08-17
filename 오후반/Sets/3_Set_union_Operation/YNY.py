# Enter your code here. Read input from STDIN. Print output to STDOUT
Eng_num = int(input())
Eng_stu = set(input().split())
Fran_num = int(input())
Fran_stu = set(input().split())

ans=Eng_stu.union(Fran_stu)
print (len(ans))
