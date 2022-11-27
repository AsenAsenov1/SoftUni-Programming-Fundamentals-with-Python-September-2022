price_ratings = list(map(int, input().split(", ")))
entry_point_index = int(input())
items_to_break = input()

left = []
right = []

if items_to_break == "cheap":

    for item in range(len(price_ratings)):
        entry_number = price_ratings[entry_point_index]
        if item < entry_point_index:
            if price_ratings[item] < entry_number:
                left.append(price_ratings[item])

        elif item == entry_point_index:
            continue

        elif item > entry_point_index:
            entry_number = price_ratings[entry_point_index]
            if price_ratings[item] < entry_number:
                right.append(price_ratings[item])

elif items_to_break == "expensive":
    for item in range(len(price_ratings)):
        entry_number = price_ratings[entry_point_index]
        if item < entry_point_index:
            if price_ratings[item] >= entry_number:
                left.append(price_ratings[item])

        elif item == entry_point_index:
            continue

        elif item > entry_point_index:
            entry_number = price_ratings[entry_point_index]
            if price_ratings[item] >= entry_number:
                right.append(price_ratings[item])

sum_left = sum(left)
sum_right = sum(right)

if sum_left > sum_right:
    print(f"Left - {sum_left}")
elif sum_left == sum_right:
    print(f"Left - {sum_right}")
else:
    print(f"Right - {sum_right}")
