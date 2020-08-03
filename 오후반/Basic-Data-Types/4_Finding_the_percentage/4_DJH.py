if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=0
    for i in range(3):
        a= a + float(student_marks[query_name][i])
    print("%0.2f" % float(a/3))
