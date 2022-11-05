numbers = list(map(int, input().split()))
middle_index = len(numbers) // 2

left_car_nums = numbers[:middle_index]
left_car_score = 0
for left_num in left_car_nums:
    if left_num == 0:
        left_car_score *= 0.8
    left_car_score += left_num

right_car_score = 0
right_car_nums = list(reversed(numbers[middle_index + 1:]))
for right_num in right_car_nums:
    if right_num == 0:
        right_car_score *= 0.8
    right_car_score += right_num

if left_car_score <= right_car_score:
    print(f"The winner is left with total time: {round(left_car_score, 1)}")
else:
    print(f"The winner is right with total time: {round(right_car_score, 1)}")
