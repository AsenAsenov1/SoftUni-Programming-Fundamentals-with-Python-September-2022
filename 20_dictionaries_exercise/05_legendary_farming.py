materials_dict = {}
legendary_dict = {"shards": 0, "fragments": 0, "motes": 0}
found_item = False

while not found_item:
    initial_lst_materials = input().split()

    for x in range(1, len(initial_lst_materials), 2):
        item = (initial_lst_materials[x]).lower()
        value = int(initial_lst_materials[x - 1])

        if item == "motes" or item == "shards" or item == "fragments":
            legendary_dict[item] += value
        else:
            if item not in materials_dict.keys():
                materials_dict[item] = 0
            materials_dict[item] += value

        if not found_item:
            if legendary_dict["shards"] >= 250:
                legendary_dict["shards"] -= 250
                print("Shadowmourne obtained!")
                found_item = True
                break

            elif legendary_dict["fragments"] >= 250:
                legendary_dict["fragments"] -= 250
                print("Valanyr obtained!")
                found_item = True
                break

            elif legendary_dict["motes"] >= 250:
                legendary_dict["motes"] -= 250
                print("Dragonwrath obtained!")
                found_item = True
                break

print(f'shards: {legendary_dict["shards"]}')
print(f'fragments: {legendary_dict["fragments"]}')
print(f'motes: {legendary_dict["motes"]}')

for item, value in materials_dict.items():
    print(f"{item}: {value}")

