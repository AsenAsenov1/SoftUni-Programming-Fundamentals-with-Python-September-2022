number_of_cities = int(input())

total_money_earned = 0
total_expenses = 0

for city_counter in range(1, number_of_cities + 1):
    city_name = input()
    money_earned = float(input())
    expenses = float(input())

    current_money_earned = 0
    current_expenses = 0
    current_profit = 0

    if city_counter % 5 == 0:
        money_earned *= 0.90

    if city_counter % 3 == 0:
        if city_counter % 5 != 0:  # само ако не вали --> special event
            expenses *= 1.50

    current_money_earned += money_earned
    current_expenses += expenses
    current_profit = current_money_earned - current_expenses

    total_money_earned += current_money_earned
    total_expenses += current_expenses

    print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")

profit = total_money_earned - total_expenses
print(f"Burger Bus total profit: {profit:.2f} leva.")
