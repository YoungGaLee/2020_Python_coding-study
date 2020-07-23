num_info=int(input())
dic={}

for i in range(num_info):
    name,num = input().strip().split(' ')
    dic[name] = num


for j in range(num_info):
    q = input()
    try:
        print(q+ '=' + dic[q])
    except:
        print('Not found')
