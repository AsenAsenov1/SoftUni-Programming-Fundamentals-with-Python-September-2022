def absolute_value():
    number_list = list(map(float, initial_list))
    return list(map(abs, number_list))


initial_list = input().split()
print(absolute_value())
