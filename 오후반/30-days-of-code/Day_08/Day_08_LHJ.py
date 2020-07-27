n = int(input())
a = {}
for i in range(0, n):
    name_num = input().split()
    for j in range(0, len(name_num)):
        a[name_num[0]] = name_num[1]

for k in range(0, n):
    c = input()

    if (c in a) == True:
        print('%s=%s' % (c, a[c]))
    else:
        print('Not found')