import re

expression = r"(\d{2})([\/\.\-])([A-Z][a-z]{2})\2(\d{4})"

text = input()

match = re.findall(expression, text)

for data in match:
    print(f"Day: {data[0]}, Month: {data[2]}, Year: {data[3]}")
