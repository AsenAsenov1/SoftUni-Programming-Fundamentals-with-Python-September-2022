items_and_prices = input().split("|")
budget = float(input())
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
ticket_price = 150
markup = 0.40  # покачва цената на стоката с 40 %
new_items_price = []
profit = 0

for item in items_and_prices:
    current_stock = item.split("->")
    current_item = current_stock[0]
    current_price = float(current_stock[1])

    if current_item == "Clothes":
        if current_price <= clothes_max_price:
            if budget - current_price >= 0:
                budget -= current_price
                sold_item_price = (current_price * markup) + current_price
                new_items_price.append(round(sold_item_price, 2))
                profit += sold_item_price - current_price

    elif current_item == "Shoes":
        if current_price <= shoes_max_price:
            if budget - current_price >= 0:
                budget -= current_price
                sold_item_price = (current_price * markup) + current_price
                new_items_price.append(round(sold_item_price, 2))
                profit += sold_item_price - current_price

    elif current_item == "Accessories":
        if current_price <= accessories_max_price:
            if budget - current_price >= 0:
                budget -= current_price
                sold_item_price = (current_price * markup) + current_price
                new_items_price.append(round(sold_item_price, 2))
                profit += sold_item_price - current_price

total = sum(new_items_price) + budget

print(*new_items_price)
print(f"Profit: {profit:.2f}")
if total >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
