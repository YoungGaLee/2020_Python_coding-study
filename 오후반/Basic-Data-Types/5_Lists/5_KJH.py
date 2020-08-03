
if __name__ == '__main__':
    N = int(input())
    blank=[]
    for _ in range(N):
        x = input().split(" ")
        cmd = x[0]
        if cmd == 'insert':
            blank.insert(int(x[1]), int(x[2]))
        elif cmd == 'print':
            print(blank)        
        elif cmd == 'remove':
            blank.remove(int(x[1]))        
        elif cmd == 'append':
            blank.append(int(x[1]))
        elif cmd == 'sort':
            blank == blank.sort()
        elif cmd == 'pop':
            blank.pop()
        elif cmd == 'reverse':
            blank == blank.reverse() 
