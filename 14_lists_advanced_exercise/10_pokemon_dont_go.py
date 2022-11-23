sequence = list(map(int, input().split()))
popped_nums = []

while sequence:
    index = int(input())
    if index < 0:
        value = sequence[0]
        sequence[0] = sequence[-1]
    elif index >= len(sequence):
        value = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        value = sequence.pop(index)
    popped_nums.append(value)
    sequence = [(x + value) if x <= value else (x - value) for x in sequence]

print(sum(popped_nums))
