def min_max_sum(some_list):
    result = (
        f"The minimum number is {min(some_list)}\n"
        f"The maximum number is {max(some_list)}\n"
        f"The sum number is: {sum(some_list)}\n")
    return result


input_list = input().split()
integer_list = list(map(int, input_list))
print(min_max_sum(integer_list))
