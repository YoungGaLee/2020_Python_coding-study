if __name__ == '__main__':
    
    student = {}
    ans = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name] = score
    S = list(set(student.values()))
    S.sort()
    ans_score = S[1]

    for name, score in student.items():
        
        if score == ans_score:
            ans.append(name)
            answer = sorted(ans)
            
    for i in answer:
        print(i)

'''
if __name__ == '__main__':
    python_student = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_student.append((name,score))
        
    A = sorted(python_student, key = lambda x : x[1])
    ans_score = A[1][1]

    for name, score in python_student:
        
        if score == ans_score:
            ans.append(name)
            answer = sorted(ans)
            
    for i in answer:
        print(i)

   
    
'''
