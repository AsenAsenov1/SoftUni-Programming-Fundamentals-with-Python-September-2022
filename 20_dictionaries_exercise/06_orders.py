products_info = {}

while True:
    current_product = input().split(" ")
    if 'buy' in current_product:
        break
    product = current_product[0]
    price = float(current_product[1])
    quantity = int(current_product[2])

    if product not in products_info.keys():
        products_info[product] = [price, quantity]
    else:
        products_info[product][1] += quantity
        products_info[product][0] = price

for product, values in products_info.items():
    total_sum = products_info[product][0] * products_info[product][1]
    print(f"{product} -> {total_sum:.2f}")
