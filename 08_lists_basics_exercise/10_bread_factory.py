working_day_events = input().split("|")

coins = 100
energy = 100
closed = False

for day in working_day_events:
    splt_days = day.split("-")
    event = splt_days[0]
    number = int(splt_days[1])

    if event == "rest":
        if number + energy > 100:
            gained_energy = 100 - energy
            energy = 100
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")

    elif event == "order":
        energy -= 30
        if energy > 0:
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        ingredient = event
        if coins >= number:
            coins -= number
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            closed = True
            break

if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")