def merge_the_tools(string, k):
    
    n = int(len(string)/k)
    S = list(string)
    
    for i in range(n):
        ans = []
        part1 = S[:k]
        for i in range(k):
            if part1[i] not in ans:
                ans.append(part1[i])
                
        print("".join(ans))
        del S[:k]


if __name__ == '__main__':
