products = {}

while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    key = command[0]
    value = command[1]
    if key not in products:
        products[key] = 0
    else:
        products[key] += int(value)

print(f"Products in stock: ")

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
