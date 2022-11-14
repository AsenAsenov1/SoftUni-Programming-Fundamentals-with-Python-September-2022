numbers = list(map(int, input().split(", ")))

current_group = 10

previous_group = current_group - 10
while len(numbers) > 0:
    list_of_numbers = list(filter(lambda x: previous_group < x <= current_group, numbers))
    numbers = list(filter(lambda x: x > current_group, numbers))
    print(f"Group of {current_group}'s: {list_of_numbers}")
    current_group += 10
