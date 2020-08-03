if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score_list=list(arr)    #입력 받은 것을 list 형태로 저장

    maximum=max(score_list) #최대값
    
    num=0

    for i in range(n):  #최대값 찾아 모두 공백으로 바꿈
        if score_list[i]==maximum: 
            score_list[i]=''
            num+=1
    
    for j in range(num):    #공백을 제거
        score_list.remove('')
    
    print(max(score_list))  #두번째 최대값
