T = int(input())
for k in range(T):
    S = input()
    L = len(S)
    count1 = "" 
    count2 = ""
    for i in range(0,L,2):
        count1 += S[i]
    
    for i in range(1,L,2):
        count2 += S[i]
    print(count1 +' '+ count2 )
        
