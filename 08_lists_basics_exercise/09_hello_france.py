items_and_prices = input().split("|")
budget = float(input())

clothes_max = 50
shoes_max = 35
accessories_max = 20.50
ticket_price = 150
items_prices = []

for item_price in items_and_prices:
    item_price = item_price.split("->")
    item = item_price[0]
    price = float(item_price[1])

    if "Clothes" in item:
        if price <= clothes_max:
            if budget - price >= 0:
                budget -= price
                items_prices.append(price)
    elif "Shoes" in item:
        if price <= shoes_max:
            if budget - price >= 0:
                budget -= price
                items_prices.append(price)
    elif "Accessories" in item:
        if price <= accessories_max:
            if budget - price >= 0:
                budget -= price
                items_prices.append(price)

sold_prices = [f"{(x * 1.4):.2f}" for x in items_prices]
profit = (sum(items_prices) * 1.4) - sum(items_prices)
budget += (sum(items_prices) * 1.4)

print(*sold_prices)
print(f"Profit: {profit:.2f}")
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
