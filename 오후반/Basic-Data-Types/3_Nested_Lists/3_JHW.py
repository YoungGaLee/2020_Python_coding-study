if __name__ == '__main__':
    grades_list=[]
    score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades_list.append([name,score])    #name과 score를 중첩된 list로 저장
        score_list.append(score)    #두번째 최소값을 찾기 위해 score만 list로 저장
    
    lowest=min(score_list)  #최소값 함수
    num=0
    
    for i in range(len(score_list)):
        if score_list[i]==lowest:   #최소값을 모두 ''로 바꿔줌
            score_list[i]=''
            num+=1
    for j in range(num):    #최소값이였던 '' 제거
        score_list.remove('')
    
    second_min=min(score_list)  #두번째 최소값

    result=[]

    for k in range(len(grades_list)):   #두번째 최소값에 해당하는 사람 이름을 결과에 저장
        if grades_list[k][1]==second_min:
            result.append(grades_list[k][0])
    
    result.sort()   #결과인 이름들을 오름차순으로 정렬 & 출력
    
    for l in range(len(result)):
        print(result[l])
