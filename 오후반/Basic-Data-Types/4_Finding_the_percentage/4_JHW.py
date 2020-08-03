if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()   #*line은 입력받을 line의 list 요소 갯수를 모를 때
        scores = list(map(float, line)) # * 을 붙임
        student_marks[name] = scores
    query_name = input()
    print('%.2f'%(sum(student_marks.get(query_name))/len(student_marks.get(query_name))))
