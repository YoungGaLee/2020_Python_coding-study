# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}

for i in range(n):
    name_num = input().split()

    name = name_num[0]
    num = name_num[1]

    phoneBook[name] = num

for j in range(n):
    try:
        phone_name = input()
        
        if phone_name in phoneBook:
            print(phone_name, '=', phoneBook[phone_name], sep = '')
        else:
            print('Not found')
    except:
        break
