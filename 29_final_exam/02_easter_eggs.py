import re

text = input()
pattern = r"[#@]{1,}([a-z]{3,})[#@]{1,}[^a-zA-Z0-9]*/{1,}(\d+)\/{1,}"

match = re.findall(pattern, text)

if match:
    for color, amount in match:
        print(f"You found {amount} {color} eggs!")
