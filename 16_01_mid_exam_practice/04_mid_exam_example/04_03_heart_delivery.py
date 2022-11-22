neighborhood_numbers = list(map(int, input().split("@")))
already_had = []
while True:
    command = input()
    if command == "Love!":
        break

    command_split = command.split()
    jump_index = int(command_split[1])

    if jump_index >= len(neighborhood_numbers):
        jump_index = 0
        if neighborhood_numbers[jump_index] <= 0:  # if current house already is 0
            print(f"Place {jump_index} already had Valentine's day.")
        else:
            neighborhood_numbers[jump_index] -= 2
            print(f"Place {jump_index} has Valentine's day.")
        continue

    for house in range(0, neighborhood_numbers[jump_index] + 1, jump_index+1):
        if house == 0:
            continue
        current_house = neighborhood_numbers[jump_index]
        # if jump_index < len(neighborhood_numbers):  # index is valid
        if current_house <= 0:  # if current house already is 0
            print(f"Place {house} already had Valentine's day.")
        else:
            neighborhood_numbers[house] -= 2 # if current house IS NOT  0
            print(f"Place {house} has Valentine's day.")
