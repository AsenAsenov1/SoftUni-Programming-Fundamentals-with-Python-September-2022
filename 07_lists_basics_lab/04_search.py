number = int(input())
filter_string = input()

unfiltered_list = []
filtered_list = []

for i in range(number):
    current_string = input()
    unfiltered_list.append(current_string)
    if filter_string in current_string:
        filtered_list.append(current_string)

print(unfiltered_list)
print(filtered_list)