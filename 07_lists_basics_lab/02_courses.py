# number of courses to add
number = int(input())

# courses list
courses_list = []

# add each course to the list
for course in range(number):
    course_to_add = input()
    courses_list.append(course_to_add)

print(courses_list)
