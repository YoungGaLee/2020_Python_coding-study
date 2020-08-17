def merge_the_tools(string, k):
    for i in range(int(len(string)/k)):
        ch = []
        for j in string[i*k:i*k+k]:
            if j in ch:
                continue
            ch.append(j)
            print(j, end='')
        print()


