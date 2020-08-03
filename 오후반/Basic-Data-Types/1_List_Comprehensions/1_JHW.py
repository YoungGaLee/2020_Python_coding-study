from itertools import product

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x_list=list(range(x+1)) #x=1일 때 x_list=[0,1]
    y_list=list(range(y+1))
    z_list=list(range(z+1))
    
    items=[x_list,y_list,z_list]    #[[0,1],[0,1],[0,1]]
    
    my_list=list(product(*items))   #조합을 구해주는 intertools.product 함수

    new_list=[0]*(len(my_list))    #my_list와 같은 자리수를 갖는 new_list 선언

    for l in range(len(my_list)):   #product 함수는 list 형태로 결과 나오지만 요소는 
        new_list[l]=list(my_list[l])    #튜플이므로 [(0,0,0),(0,0,1),...]를 list로 변환
    
    num=0   #총합이 n인 요소들의 갯수
    
    for m in range(len(new_list)):  #총합인 n인 요소들을 0으로 바꿔주고 갯수를 셈
        if sum(new_list[m])==n:
            new_list[m]=0
            num+=1

    for o in range(num):    #0으로 바뀐 요소들을 삭제
        new_list.remove(0)
    
    print(new_list)
