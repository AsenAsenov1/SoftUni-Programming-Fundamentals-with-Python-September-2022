def positive(number_lst):
    positive_numbers = [x for x in number_lst if x >= 0]
    joined = ', '.join(list(map(str, positive_numbers)))
    return f"Positive: {joined}"


def negative(number_lst):
    negative_numbers = [x for x in number_lst if x < 0]
    joined = ', '.join(list(map(str, negative_numbers)))
    return f"Negative: {joined}"


def even(number_lst):
    even_numbers = [x for x in number_lst if x % 2 == 0]
    joined = ', '.join(list(map(str, even_numbers)))
    return f"Even: {joined}"


def odd(number_lst):
    odd_numbers = [x for x in number_lst if x % 2 != 0]
    joined = ', '.join(list(map(str, odd_numbers)))
    return f"Odd: {joined}"


input_numbers = list(map(int, input().split(", ")))

print(positive(input_numbers))
print(negative(input_numbers))
print(even(input_numbers))
print(odd(input_numbers))
