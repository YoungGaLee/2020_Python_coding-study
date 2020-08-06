from itertools import product

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    xList = []
    yList = []
    zList = []
    allList = []

    for i in range(x + 1):
        xList.append(i)
    allList.append(xList)

    for i in range(y + 1):
        yList.append(i)
    allList.append(yList)

    for i in range(z + 1):
        zList.append(i)
    allList.append(zList)

    per = list(product(*allList))  # 조합 만들기
    perList = []
    for tmp in per:
        perList.append(list(tmp))  # 튜플 형태의 조합을 리스트로
        
    perList_=perList.copy()
    
    for i in perList:
        if sum(i) == n:
            perList_.remove(i)
    print(perList_)
