# 1번 Runtime error

n = int(input()) 
dic = {}

for _ in range(n): 
    name, phoneNumber = input().split()
    dic[name] = phoneNumber

P = dic.keys()

for _ in range(n): 
    person = input() 

    if person in P: 
        number = dic[person]
        print("{}={}".format(person, number)) 

    else: 
        print("Not found")
        
