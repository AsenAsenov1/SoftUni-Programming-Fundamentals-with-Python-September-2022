zoo_animals = {}
area_counter = []
count_dictionary = {}
while True:
    command = input()
    if "EndDay" in command:
        break

    command = command.split()
    action = command[0]
    animal_info = command[1].split("-")
    if "Add" in action:
        animal_name, food, place = animal_info
        if animal_name not in zoo_animals:
            zoo_animals[animal_name] = {"food": int(food), "place": place}
        else:
            zoo_animals[animal_name]["food"] += int(food)

    elif "Feed" in action:
        animal_name, food = animal_info
        if animal_name in zoo_animals:
            zoo_animals[animal_name]["food"] -= int(food)
            if zoo_animals[animal_name]["food"] <= 0:
                zoo_animals.pop(animal_name)
                print(f"{animal_name} was successfully fed")

for place in zoo_animals.values():
    area_counter.append(place['place'])
count_dictionary = {place: area_counter.count(place) for place in area_counter}

print("Animals:")
for name, food in zoo_animals.items():
    print(f"{name} -> {food['food']}g")

print("Areas with hungry animals:")
for area, amount in count_dictionary.items():
    print(f"{area}: {amount}")
