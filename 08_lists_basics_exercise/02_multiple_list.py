factor = int(input())
count = int(input())

new_list = []

for item in range(1, count + 1):
    new_list.append(item * factor)

print(new_list)
