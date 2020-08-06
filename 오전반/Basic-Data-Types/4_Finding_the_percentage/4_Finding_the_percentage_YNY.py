if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    q_score=student_marks[query_name]
    ans=sum(q_score)/len(q_score)
    print('%.2f' %ans)
