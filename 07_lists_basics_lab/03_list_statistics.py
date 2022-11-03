# count of numbers to add
numbers = int(input())

# lists for positive and negative numbers
positive_numbers = []
negative_numbers = []

for current_number in range(numbers):
    input_number = int(input())
    if input_number >= 0:
        positive_numbers.append(input_number)
    else:
        negative_numbers.append(input_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")