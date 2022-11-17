initial_array = input().split()

while True:
    command = input()
    if command == "end":
        break
    command_split = command.split()
    action = command_split[0]

    if action == "swap":
        index_1 = int(command_split[1])
        index_2 = int(command_split[2])
        initial_array[index_1], initial_array[index_2] = initial_array[index_2], initial_array[index_1]

    elif action == "multiply":
        multi_1 = int(command_split[1])
        multi_2 = int(command_split[2])
        result = int(initial_array[multi_1]) * int(initial_array[multi_2])
        initial_array.pop(multi_1)
        initial_array.insert(multi_1, result)

    elif action == "decrease":
        initial_array = [int(x) - 1 for x in initial_array]

initial_array = list(map(str, initial_array))
print(", ".join(initial_array))
