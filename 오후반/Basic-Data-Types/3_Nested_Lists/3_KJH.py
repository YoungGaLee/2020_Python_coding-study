import operator
students, scores = [], []

if __name__ == '__main__':
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name,score])
    number=sorted(list(set(scores)))[1]
    students.sort(key=operator.itemgetter(0))

    for i in range(n):
        if students[i][1]==number:
            print(students[i][0])
