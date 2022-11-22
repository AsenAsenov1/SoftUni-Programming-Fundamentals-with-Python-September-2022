initial_list = input().split("!")
command = input()

while command != "Go Shopping!":
    action = command.split(" ")
    item = action[1]

    if action[0] == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)

    if action[0] == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)

    if action[0] == "Correct":
        if item in initial_list:
            new_item = action[2]
            index = initial_list.index(item)
            initial_list[index] = new_item

    if action[0] == "Rearrange":
        if item in initial_list:
            index = initial_list.index(item)
            move = initial_list.pop(index)
            initial_list.append(move)

    command = input()

print(", ".join(initial_list))
