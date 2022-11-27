travel_route = input().split("||")

fuel_amount = int(input())
ammunition = int(input())

for current_command in travel_route:
    section = current_command.split()
    action = section[0]

    if action == "Travel":
        number = int(section[1])
        fuel_amount -= number
        if fuel_amount >= 0:
            print(f'The spaceship travelled {number} light-years.')
        else:
            print("Mission failed.")
            break

    elif action == "Enemy":
        number = int(section[1])
        if ammunition >= number:
            ammunition -= number
            print(f"An enemy with {number} armour is defeated.")
        else:
            left_fuel = fuel_amount - (number * 2)
            if left_fuel >= 0:
                print(f"An enemy with {number} armour is outmaneuvered.")
                fuel_amount -= number * 2
            else:
                print("Mission failed.")
                break

    elif action == "Repair":
        number = int(section[1])
        ammo_added = number * 2
        fuel_amount += number
        ammunition += ammo_added
        print(f"Ammunitions added: {ammo_added}.")
        print(f"Fuel added: {number}.")

    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
