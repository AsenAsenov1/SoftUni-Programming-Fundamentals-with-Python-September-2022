sequence_of_targets = list(map(int, input().split()))
in_range = False

while True:
    command = input()
    if command == "End":
        break

    split_command = command.split()
    action = split_command[0]
    index = int(split_command[1])

    if action == "Shoot":
        power = int(split_command[2])
        if -len(sequence_of_targets) <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] < 1:
                sequence_of_targets.pop(index)

    elif action == "Add":
        value = int(split_command[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
            continue

    elif action == "Strike":
        radius = int(split_command[2])
        start = index - radius
        stop = index + radius
        if 0 <= start < len(sequence_of_targets):
            if 0 <= stop < len(sequence_of_targets):
                in_range = True
                targets_to_remove = sequence_of_targets[start:stop+1]
                # print(targets_to_remove)
                sequence_of_targets = [x for x in sequence_of_targets if x not in targets_to_remove]
                continue

        if not in_range:
            print("Strike missed!")
            continue

sequence_of_targets = list(map(str, sequence_of_targets))
print("|".join(sequence_of_targets))