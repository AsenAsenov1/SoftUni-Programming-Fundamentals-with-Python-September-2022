number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000:
        continue
    else:
        price_coffee = price_capsule * days * capsules
        total_price += price_coffee
        print(f"The price for the coffee is: ${price_coffee:.2f}")

print(f"Total: ${total_price:.2f}")
