def sum_of_odd_and_even(number1):
    even_list = []
    odd_list = []
    for num in number1:
        if int(num) % 2 == 0:
            even_list.append(int(num))
        else:
            odd_list.append(int(num))
    even_sum = sum(even_list)
    odd_sum = sum(odd_list)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


input_number = input()

print(sum_of_odd_and_even(input_number))
