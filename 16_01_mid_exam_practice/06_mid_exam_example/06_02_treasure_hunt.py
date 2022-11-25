initial_loot = input().split("|")
failed = False
while True:
    command = input()
    if command == "Yohoho!":
        break
    command_split = command.split()
    action = command_split[0]

    if action == "Loot":
        items = command_split[1::]
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif action == "Drop":
        index = int(command_split[1])
        if -len(initial_loot) <= index < len(initial_loot):
            item = initial_loot.pop(index)
            initial_loot.append(item)

    elif action == "Steal":
        num_of_items_to_remove = int(command_split[1])
        if num_of_items_to_remove < len(initial_loot):
            stolen_items = initial_loot[-num_of_items_to_remove:]
            initial_loot = initial_loot[:-num_of_items_to_remove]
            print(", ".join(stolen_items))
        else:
            print(", ".join(initial_loot))
            print("Failed treasure hunt.")
            failed = True

if not failed:
    avg_sum = len("".join(initial_loot)) / len(initial_loot)
    print(f"Average treasure gain: {avg_sum:.2f} pirate credits.")

