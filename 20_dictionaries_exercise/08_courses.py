courses_info = {}

while True:
    command = input().split(":")
    if 'end' in command:
        break
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses_info.keys():
        courses_info[course_name] = []
    courses_info[course_name].append(student_name)

for courses, students in courses_info.items():
    print(f"{courses}: {len(students)}")
    for student in students:
        print(f"--{student}")
