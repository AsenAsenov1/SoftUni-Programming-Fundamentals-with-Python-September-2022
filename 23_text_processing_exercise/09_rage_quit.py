import re

pattern = r"(\D*)(\d{1,2})"

text = input().upper()
match = re.findall(pattern, text)
multiply = [x[0] * int(x[1]) for x in match]
final_word = "".join(multiply)
symbols = len(set(final_word))

print(f"Unique symbols used: {symbols}")
print(final_word)
