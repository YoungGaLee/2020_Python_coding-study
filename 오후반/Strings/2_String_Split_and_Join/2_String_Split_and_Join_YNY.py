def split_and_join(line):
    ans=''
    s=line.split(" ")
    for i in s:
        ans+=i
        ans+='-'
    return ans[:-1]
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
