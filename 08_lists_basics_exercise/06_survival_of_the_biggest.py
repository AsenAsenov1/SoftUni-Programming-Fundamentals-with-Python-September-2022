simple_list = input().split(" ")
numbers_to_remove = int(input())

list_of_nums = []
list_of_chars = []

for char in simple_list:
    list_of_nums.append(int(char))

for number in range(numbers_to_remove):
    lowest_number = min(list_of_nums)
    list_of_nums.remove(lowest_number)

for chars in list_of_nums:
    list_of_chars.append(str(chars))

print(", ".join(list_of_chars))
