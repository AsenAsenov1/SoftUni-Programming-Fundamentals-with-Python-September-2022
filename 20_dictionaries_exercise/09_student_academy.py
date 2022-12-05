rows = int(input())
academy_grades = {}

for i in range(rows):
    student = input()
    grade = float(input())

    if student not in academy_grades.keys():
        academy_grades[student] = [grade]
    else:
        academy_grades[student].append(grade)

for student_academy, grades_academy in academy_grades.items():
    average_grade = sum(grades_academy) / len(grades_academy)
    if average_grade >= 4.50:
        print(f'{student_academy} -> {average_grade:.2f}')

