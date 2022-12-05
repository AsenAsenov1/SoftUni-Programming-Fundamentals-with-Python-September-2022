number_of_commands = int(input())
parking_info = {}

for x in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    name = current_command[1]

    if action == "register":
        license_plate = current_command[2]
        if name in parking_info.keys():
            print(f"ERROR: already registered with plate number {parking_info[name][1]}")
        else:
            parking_info[name] = [name, license_plate]
            print(f"{name} registered {license_plate} successfully")

    elif action == "unregister":
        if name not in parking_info.keys():
            print(f"ERROR: user {name} not found")
        else:
            parking_info.pop(name)
            print(f"{name} unregistered successfully")

for person, car_info in parking_info.items():
    print(f"{person} => {car_info[1]}")
