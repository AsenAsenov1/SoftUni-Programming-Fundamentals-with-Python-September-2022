number_of_cars = int(input())
cars_info = {}
for i in range(number_of_cars):
    car, mileage, fuel_available = input().split("|")
    cars_info[car] = {"mileage": int(mileage), "fuel": int(fuel_available)}

while True:
    command = input()
    if "Stop" in command:
        break
    action = command.split(" : ")

    if "Drive" in action:
        car, distance, fuel = action[1:]
        if cars_info[car]["fuel"] - int(fuel) < 1:
            print("Not enough fuel to make that ride")
        else:
            cars_info[car]["fuel"] -= int(fuel)
            cars_info[car]["mileage"] += int(distance)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_info[car]["mileage"] > 100000:
            cars_info.pop(car)
            print(f"Time to sell the {car}!")

    elif "Refuel" in action:
        car, fuel = action[1:]
        max_fuel_capacity = 75
        if cars_info[car]["fuel"] + int(fuel) > max_fuel_capacity:
            refill_amount = max_fuel_capacity - cars_info[car]["fuel"]
            cars_info[car]["fuel"] = max_fuel_capacity
            print(f"{car} refueled with {refill_amount} liters")
        else:
            cars_info[car]["fuel"] += int(fuel)
            print(f"{car} refueled with {fuel} liters")

    elif "Revert" in action:
        car, kilometers = action[1:]
        if cars_info[car]["mileage"] - int(kilometers) < 10000:
            cars_info[car]["mileage"] = 10000
        else:
            cars_info[car]["mileage"] -= int(kilometers)
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, mileage_fuel in cars_info.items():
    print(f"{car} -> Mileage: {mileage_fuel['mileage']} kms, Fuel in the tank: {mileage_fuel['fuel']} lt.")
