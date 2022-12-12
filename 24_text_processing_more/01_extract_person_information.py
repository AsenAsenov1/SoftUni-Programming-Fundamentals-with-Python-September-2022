number = int(input())

for i in range(number):
    current_name = input()
    start_index_name = 0
    stop_index_name = 0
    start_age = 0
    stop_age = 0
    for char in current_name:
        if char == "@":
            start_index_name = current_name.index(char)
        elif char == "|":
            stop_index_name = current_name.index(char)
        elif char == "#":
            start_age = current_name.index(char)
        elif char == "*":
            stop_age = current_name.index(char)
    name = current_name[start_index_name + 1:stop_index_name]
    age = current_name[start_age + 1:stop_age]
    print(f"{name} is {age} years old.")
