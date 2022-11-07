def even_num_filter(number):
    if number % 2 == 0:
        return True

    return False


input_nums = input().split()
list_nums = list(map(int, input_nums))
filtered_nums = list(filter(even_num_filter, list_nums))

print(filtered_nums)
