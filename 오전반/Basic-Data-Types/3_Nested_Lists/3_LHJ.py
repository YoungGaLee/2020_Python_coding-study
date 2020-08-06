students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])

result = []
for i in students:
    if min(students)[0] < i[0]:
        result.append(i)
a = []
for i in result:
    if min(result)[0] == i[0]:
        a.append(i[1])
a.sort()
for i in a:
    print(i)