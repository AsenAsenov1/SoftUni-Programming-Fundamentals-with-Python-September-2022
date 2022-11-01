number_of_lines = int(input())

total_sum = 0

for chars in range(number_of_lines):
    characters = input()
    total_sum += ord(characters)

print(f"The sum equals: {total_sum}")
