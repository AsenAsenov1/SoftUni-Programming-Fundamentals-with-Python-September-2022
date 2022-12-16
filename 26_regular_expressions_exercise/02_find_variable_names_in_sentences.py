import re

current_string = input()
pattern = r"\b\_([A-Za-z0-9]+)\b\s?"
match = re.findall(pattern, current_string)

if match:
    print(",".join(match))
