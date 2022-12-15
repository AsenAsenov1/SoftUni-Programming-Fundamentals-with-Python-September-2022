import re

names = input()
regex_pattern = r"(\b[A-Z][a-z]+\b)[ ](\b[A-Z][a-z]+\b)"

matches = re.findall(regex_pattern, names)

for name in matches:
    print(" ".join(name), end=" ")
