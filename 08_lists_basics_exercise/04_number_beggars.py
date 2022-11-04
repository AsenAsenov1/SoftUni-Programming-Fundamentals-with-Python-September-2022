beggars_list = input().split(", ")
beggars_count = int(input())

sum_list = []
total_sum = 0
starting_index = 0

while starting_index < beggars_count:
    total_sum = 0
    for index in range(starting_index, len(beggars_list), beggars_count):
        price = int(beggars_list[index])
        total_sum += price
    starting_index += 1
    sum_list.append(total_sum)

print(sum_list)
