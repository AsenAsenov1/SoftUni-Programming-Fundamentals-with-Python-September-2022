import re

text = input().lower()
word = input().lower()
pattern = rf"\b{word}\b"

match = re.findall(pattern, text)

print(len(match))