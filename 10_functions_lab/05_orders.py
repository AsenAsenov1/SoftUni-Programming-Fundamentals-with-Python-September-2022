def order_total_sum(product: str, count: int):
    price = 0
    if "coffee" in product:
        price = 1.50
    elif "water" in product:
        price = 1.00
    elif "coke" in product:
        price = 1.40
    elif "snacks" in product:
        price = 2.00
    total_price = f"{price * count:.2f}"

    return total_price


drink = input()
quantity = int(input())
order_input = order_total_sum(drink, quantity)
print(order_input)
