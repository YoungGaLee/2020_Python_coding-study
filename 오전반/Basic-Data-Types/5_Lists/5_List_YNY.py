if __name__ == '__main__':
    N = int(input())
    q_query=[]
    ans=[]
    for i in range(N):
        q_query.append(input().split())

    for i in q_query:
        if i[0]=='insert':
            ans.insert(int(i[1]),int(i[2]))
        elif i[0]=='print':
            print(ans)
        elif i[0]=='remove':
            ans.remove(int(i[1]))
        elif i[0]=='append':
            ans.append(int(i[1]))
        elif i[0]=='sort':
            ans.sort()
        elif i[0]=='pop':
            ans.pop()
        elif i[0]=='reverse':
            ans.reverse()
