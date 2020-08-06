if __name__ == '__main__':
    n = int(input())#학생수
    student_marks = {}#학생점수딕셔너리
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))#점수는 list로 받음
        student_marks[name] = scores#딕셔너리로 이름-점수
        
    query_name = input()
    a = sum(student_marks[query_name])/len(student_marks[query_name])
    
    print('%.2f'%(a))
