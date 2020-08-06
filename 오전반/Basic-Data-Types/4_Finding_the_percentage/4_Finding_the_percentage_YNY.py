if __name__ == '__main__':

    tmp = []
    studentList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tmp.append(name)
        tmp.append(score)
        studentList.append(tmp)
        tmp = []

    SortedStudentList = sorted(studentList, key=lambda x: x[1])

    for i in range(len(SortedStudentList) - 1):
        MinScore = SortedStudentList[i][1]
        if SortedStudentList[i][1] == SortedStudentList[i + 1][1]:
            SecondMinScore = SortedStudentList[i + 1][1]
            continue
        else:
            SecondMinScore = SortedStudentList[i + 1][1]
            break

    ans = []
    for i in range(len(SortedStudentList)):
        if SortedStudentList[i][1] == SecondMinScore:
            ans.append(SortedStudentList[i][0])

    ans.sort()
    for i in ans:
        print(i)
