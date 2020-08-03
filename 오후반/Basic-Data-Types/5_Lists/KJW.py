if __name__ == '__main__':
    N = int(input())
    T = int(raw_input())

    L=[]
    for t in range(T):
        args = raw_input().split(" ")
        if args[0] == "append":
            L.append(int(args[1]))
        elif args[0] == "insert":
            L.insert(int(args[1]), int(args[2]))
        elif args[0] =="remove":
            L.remove(int(args[1]))
        elif args[0] == "pop":
            L. POP()
        elif args[0] == "sort":
            L.sort()
        elif args[0] == "reverse":
            L.reverse()
        elif args[0] == "print":
            print (L)
