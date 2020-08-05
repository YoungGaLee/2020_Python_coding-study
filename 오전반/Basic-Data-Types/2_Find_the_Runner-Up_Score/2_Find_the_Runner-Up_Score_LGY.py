#모든 값들을 지워주지는 않고 가장 먼저 발견된 요소를 지워준다. : remove >> set

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    
    arr.sort()
    
    print(arr[-2])
    
