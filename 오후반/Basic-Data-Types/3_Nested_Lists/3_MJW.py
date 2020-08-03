if __name__ == '__main__':
    python_students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

    python_students = sorted(python_students, key=lambda x: x[0])
    
    score_list = sorted(set([x[1] for x in python_students]))
    second_lowest_score = score_list[1]

    for (name, score) in python_students:
        if score == second_lowest_score:
            print(name)

