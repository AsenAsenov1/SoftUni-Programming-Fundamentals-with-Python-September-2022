items_dictionary = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    item = command
    if item not in items_dictionary:
        items_dictionary[item] = 0
    items_dictionary[item] += quantity

for key, value in items_dictionary.items():
    print(f"{key} -> {value}")