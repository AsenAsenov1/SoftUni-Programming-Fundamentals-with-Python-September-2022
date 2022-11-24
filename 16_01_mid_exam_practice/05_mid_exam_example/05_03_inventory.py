inventory = input().split(", ")
command = input()

while command != "Craft!":
    action = command.split(" - ")
    item = action[1]

    if action[0] == "Collect":
        if action[1] not in inventory:
            inventory.append(item)

    elif action[0] == "Drop":
        if item in inventory:
            inventory.remove(item)

    elif action[0] == "Combine Items":
        find_items = item.split(":")
        old_item = find_items[0]
        new_item = find_items[1]
        if old_item in inventory:
            index = inventory.index(old_item) + 1
            inventory.insert(index, new_item)

    elif action[0] == "Renew":
        if item in inventory:
            index_item = inventory.index(item)
            item_to_move = inventory.pop(index_item)
            inventory.append(item_to_move)

    command = input()

print(", ".join(inventory))
