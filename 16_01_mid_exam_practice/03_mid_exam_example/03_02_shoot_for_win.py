target_sequence = list(map(int, input().split()))
shot_targets_total = 0

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if -len(target_sequence) <= index < len(target_sequence):
        shot_target_value = target_sequence[index]
        target_sequence[index] = -1
        for i in range(len(target_sequence)):
            current_tar = target_sequence[i]
            if current_tar != -1:
                if current_tar > shot_target_value:
                    target_sequence[i] -= shot_target_value
                elif current_tar <= shot_target_value:
                    target_sequence[i] += shot_target_value

        shot_targets_total += 1

print(f"Shot targets: {shot_targets_total} -> {' '.join(list(map(str, target_sequence)))}")

