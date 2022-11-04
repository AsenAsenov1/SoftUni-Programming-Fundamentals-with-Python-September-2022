values = input().split(" ")

opposite = []
for num in range(len(values)):
    current = int(values[num])
    opposite.append(-current)

print(opposite)
