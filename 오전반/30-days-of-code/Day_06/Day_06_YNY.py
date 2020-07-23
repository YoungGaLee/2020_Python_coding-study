n=int(input())
q_odd=[]
q_even=[]
for i in range (n):
    q=str(input())
    for j in range(len(q)):
        if j%2==0:
            q_odd.append(q[j])
        if j%2==1:
            q_even.append(q[j])
    print("".join(q_odd) ,"".join(q_even))
    q_odd,q_even=[],[]
