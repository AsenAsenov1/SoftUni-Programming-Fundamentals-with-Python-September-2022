import re

command = input()
symbols = []
pattern = r"\d+"
while command:
    symbols.append(command)
    command = input()

for data in symbols:
    digits = re.findall(pattern, data)
    if digits:
        print(*digits, end=" ")
