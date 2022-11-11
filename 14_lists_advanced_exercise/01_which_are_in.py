first_input = input().split(", ")
second_input = input().split(", ")

filtered = []

for substring in first_input:
    for current_string in second_input:
        if substring in current_string:
            if substring not in filtered:
                filtered.append(substring)

print(filtered)
