pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health_capacity_for_section = int(input())
sunken = False

while True:
    command = input()
    if command == "Retire":
        break
    split_command = command.split()
    action = split_command[0]

    if action == "Fire":
        index = int(split_command[1])
        damage = int(split_command[2])
        if index in range(len(warship_status)):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                sunken = True
                break

    elif action == "Defend":
        start = int(split_command[1])
        stop = int(split_command[2])
        damage = int(split_command[3])
        if start in range(len(pirate_ship_status)) and stop in range(len(pirate_ship_status)):
            for section in range(start, stop + 1):
                pirate_ship_status[section] -= damage
                if pirate_ship_status[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    sunken = True
                    break

    elif action == "Repair":
        index = int(split_command[1])
        health = int(split_command[2])
        if index in range(len(pirate_ship_status)):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_capacity_for_section:
                pirate_ship_status[index] = max_health_capacity_for_section

    elif action == "Status":
        factor = max_health_capacity_for_section * 0.20  # 20% from max capacity
        count = len([x for x in pirate_ship_status if x < factor])
        print(f"{count} sections need repair.")

if not sunken:
    pirate_sum = sum(pirate_ship_status)
    war_sum = sum(warship_status)
    print(f"Pirate ship status: {pirate_sum}")
    print(f"Warship status: {war_sum}")
