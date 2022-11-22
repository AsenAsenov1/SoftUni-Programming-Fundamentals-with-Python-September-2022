quantity_of_food_kg = float(input())
quantity_of_hay_kg = float(input())
quantity_cover_kg = float(input())
pig_weight_kg = float(input())

for day in range(1, 31):
    quantity_of_food_kg -= 0.3
    if day % 2 == 0:
        quantity_of_hay_kg -= quantity_of_food_kg * 0.05  # 5 % от храната
    if day % 3 == 0:
        quantity_cover_kg -= (pig_weight_kg / 3)

food = f"{quantity_of_food_kg:.2f}"

if float(food) > 0 < quantity_of_hay_kg > 0 < quantity_cover_kg:
    print(
        f"Everything is fine! Puppy is happy! Food: {quantity_of_food_kg:.2f}, Hay: {quantity_of_hay_kg:.2f}, "
        f"Cover: {quantity_cover_kg:.2f}.")
else:
    print("Merry must go to the pet store!")
