
def METHOD(method):
    
    if method[0] == 'insert':
        List.insert(int(method[1]),int(method[2]))
    elif method[0] == 'remove':
        List.remove(int(method[1]))
    elif method[0] == 'append':
        List.append(int(method[1]))
    elif method[0] == 'sort':
        List.sort()
    elif method[0] == 'pop':
        List.pop()
    elif method[0] == 'reverse':
        List.reverse()
    elif method[0] == 'print':
        print(List)

    return 0


List = []
N = int(input())

for i in range(N):
    
    method = input().split()
    METHOD(method)        

           



    

