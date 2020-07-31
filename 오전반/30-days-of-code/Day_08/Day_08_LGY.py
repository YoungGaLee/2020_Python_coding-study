n = int(input()) 
dic = {}

for _ in range(n): 
    name, phoneNumber = input().split()
    dic[name] = phoneNumber

P = dic.keys()

state = 'keep_going'

while(state == 'keep_going'):
    try:
        person = input()

        if person in P: 
            number = dic[person]
            print("{}={}".format(person, number)) 

        else: 
            print("Not found")

    except:
        state = 'stop'
        


        
