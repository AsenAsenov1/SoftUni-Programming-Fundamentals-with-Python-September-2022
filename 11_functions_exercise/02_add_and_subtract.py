def sum_numbers(number_one, number_two):
    return number_one + number_two


def subtract(number_one, number_two):
    return number_one - number_two


def add_and_subtract(number_one, number_two, number_three):
    sum_first_second = sum_numbers(first_number, second_number)
    result = subtract(sum_first_second, third_number)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

params = first_number, second_number, third_number
print(add_and_subtract(first_number, second_number, third_number))
