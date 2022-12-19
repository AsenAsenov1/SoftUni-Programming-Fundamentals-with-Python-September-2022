number = int(input())
plants_info = {}

for i in range(number):
    plant, rarity = input().split("<->")
    plants_info[plant] = {"rarity": rarity, "rating": []}

while True:
    command = input().replace("-", "").split()
    if "Exhibition" in command:
        break

    action = command[0]
    plant = command[1]

    if plant not in plants_info.keys():
        print("error")
        continue

    if "Rate" in action:
        rating = int(command[2])
        plants_info[plant]['rating'].append(rating)
    elif "Update" in action:
        new_rarity = int(command[2])
        plants_info[plant]['rarity'] = new_rarity
    elif "Reset" in action:
        plants_info[plant]["rating"].clear()

print("Plants for the exhibition:")
for plant, values in plants_info.items():
    if len(plants_info[plant]['rating']) == 0:
        average_rating = 0
    else:
        average_rating = sum(plants_info[plant]["rating"]) / len(plants_info[plant]['rating'])
    print(f"- {plant}; Rarity: {plants_info[plant]['rarity']}; Rating: {float(average_rating):.2f}")