def round_numbers(numbers):
    return list(map(round, list_of_numbers))


initial_list = input().split()
list_of_numbers = list(map(float, initial_list))

print(round_numbers(list_of_numbers))
