if __name__ == '__main__':
    lon=[]
    los=[]
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lon.append(name)
        los.append(score)
    tdlist = [[0 for col in range(2)] for row in range(5)]
    for i in range(len(lon)):
        tdlist[i][0]=lon[i]
        tdlist[i][1]=los[i]
    for j in range(los.count(min(los))):
        los.remove(min(los))
    for k in range(len(lon)):
        if tdlist[k][1] == (min(los)):
            names.append(tdlist[k][0])
    names.sort()
    for l in range (len(names)):
        print(names[l])
