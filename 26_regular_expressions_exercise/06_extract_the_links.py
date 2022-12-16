import re

text = input()
pattern = r"(www(.[a-zA-Z]+)\.?[a-z-]+\.+[a-z]+)"

while text:
    match = re.findall(pattern, text)
    print(match)
    text = input()
