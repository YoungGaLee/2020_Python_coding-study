n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        eval("l."+cmd+"("+",".join(args)+")")
    else:
        print(l)
