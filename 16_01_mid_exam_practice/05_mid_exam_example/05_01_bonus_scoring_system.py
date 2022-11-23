from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

attendance_for_each_student = [int(input()) for x in range(number_of_students)]
total_bonus = [ceil((x / number_of_lectures) * (5 + additional_bonus)) for x in attendance_for_each_student]

print(f"Max Bonus: {max(total_bonus)}.")
print(f"The student has attended {max(attendance_for_each_student)} lectures.")

# 80/100pts.
