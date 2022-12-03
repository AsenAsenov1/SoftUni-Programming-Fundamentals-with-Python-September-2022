items_input = input().split(" ")
search_items = input().split()

count_items = {items_input[x]: items_input[x + 1] for x in range(0, len(items_input), 2)}

for item in search_items:
    if item in count_items.keys():
        print(f"We have {count_items.get(item)} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
