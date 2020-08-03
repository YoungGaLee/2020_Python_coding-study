if __name__ == '__main__':
    N = int(input())

    List = []
    for _ in range(N):
        query = input().strip().split()

        if query[0] == 'insert':
            List.insert(int(query[1]), int(query[2]))
        elif query[0] == 'print':
            print(List)
        elif query[0] == 'remove':
            idx = List.index(int(query[1]))
            List.pop(idx)
        elif query[0] == 'append':
            List.append(int(query[1]))
        elif query[0] == 'sort':
            List.sort()
        elif query[0] == 'pop':
            List.pop()
        elif query[0] == 'reverse':
            List = List[::-1]

