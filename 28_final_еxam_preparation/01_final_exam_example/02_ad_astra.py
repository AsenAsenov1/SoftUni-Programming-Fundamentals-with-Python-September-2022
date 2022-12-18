import re

data_input = input()

pattern = r"([#|]\b)([A-Za-z]+\s?[A-Za-z]*)\1\b(\d{2}\/\d{2}\/\d{2})\b\1\b(\d{1,5})\b\1"
kcal_per_day = 2000
match = re.findall(pattern,data_input)
rematch = [x[1:] for x in match]
total_calories = sum([int(x[2]) for x in rematch])
days = total_calories // kcal_per_day

print(f"You have food to last you for: {days} days!")
for product_info in rematch:
    food, year, calories = product_info
    print(f"Item: {food}, Best before: {year}, Nutrition: {calories}")

