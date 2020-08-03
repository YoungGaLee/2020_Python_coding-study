if __name__ == '__main__':
    N = int(input())
    my_list=[]
    result=[]
    for i in range(N):
        my_list.append(list(input().split()))
        if my_list[i][0]=='insert':
            result.insert(int(my_list[i][1]),int(my_list[i][2]))
        elif my_list[i][0]=='print':
            print(result)
        elif my_list[i][0]=='remove':
            result.remove(int(my_list[i][1]))
        elif my_list[i][0]=='append':
            result.append(int(my_list[i][1]))
        elif my_list[i][0]=='sort':
            result.sort()
        elif my_list[i][0]=='pop':
            result.pop()
        elif my_list[i][0]=='reverse':
            result.reverse()
