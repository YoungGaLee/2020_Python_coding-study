def ave(name):
    a = sum(student_marks[name]) / 3
    return print("%.2f"%a)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

ave(query_name)