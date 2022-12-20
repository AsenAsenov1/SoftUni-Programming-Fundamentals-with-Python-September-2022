cities_info = {}

while True:
    command = input()
    if "Sail" in command:
        break
    city, population, gold = command.split("||")
    if city not in cities_info:
        cities_info[city] = {"population": 0, "gold": 0}
    cities_info[city]["population"] += int(population)
    cities_info[city]["gold"] += int(gold)

while True:
    command = input()
    if "End" in command:
        break
    action = command.split("=>")

    if "Plunder" in action:
        town, people, gold = action[1:]
        cities_info[town]["population"] -= int(people)
        cities_info[town]["gold"] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if 0 >= cities_info[town]["population"] or cities_info[town]["gold"] <= 0:
            cities_info.pop(town)
            print(f"{town} has been wiped off the map!")

    elif "Prosper" in action:
        town, gold = action[1:]
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            cities_info[town]['gold'] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {cities_info[town]['gold']} gold.")

if cities_info:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for town, people_gold in cities_info.items():
        print(f"{town} -> Population: {people_gold['population']} citizens, Gold: {people_gold['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")