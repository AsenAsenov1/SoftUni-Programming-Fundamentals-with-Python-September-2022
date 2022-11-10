number = int(input())

train_wagons = [0] * number
command = input()

while command != "End":
    split_command = command.split()

    if "add" in split_command:
        people_to_add = int(split_command[1])
        train_wagons[-1] += people_to_add
    elif "insert" in split_command:
        index = int(split_command[1])
        people_to_add = int(split_command[2])
        train_wagons[index] += people_to_add
    elif "leave" in split_command:
        index = int(split_command[1])
        people_to_leave = int(split_command[2])
        train_wagons[index] -= people_to_leave

    command = input()

print(train_wagons)
