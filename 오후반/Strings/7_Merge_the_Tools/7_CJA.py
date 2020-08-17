def merge_the_tools(string, k):
    n = len(string)
    A = k

    for i in range(0, n, A): 
        S = string[i:i + A] #A개씩

        for j in range(len(S)):
            temp_ = sorted(set(S), key=S.index) 
            #key = 인덱스로 지정하면 인덱스 순서로 정렬
            result = ''.join(temp_)

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
