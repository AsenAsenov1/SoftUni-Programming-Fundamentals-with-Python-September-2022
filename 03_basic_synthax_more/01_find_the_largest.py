numbers = list(map(int, input()))

numbers.sort(reverse=True)

largest_number = "".join(list(map(str, numbers)))

print(largest_number)
