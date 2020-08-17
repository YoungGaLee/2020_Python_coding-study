def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s_split = string[i:i+k]
        output = ''
        for s in s_split:
            if s in output:
                continue
            output += s
        
        print(output)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
