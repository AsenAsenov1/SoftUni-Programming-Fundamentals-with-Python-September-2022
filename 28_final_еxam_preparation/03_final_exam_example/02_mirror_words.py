import re

pattern = r"([#@])\b([A-z]{3,})\b\1\1\b([A-z]+)\1"
secret_words = input()
match = re.findall(pattern, secret_words)
pairs = [" ".join(x[1:]) for x in match]
mirrored_words = [" <=> ".join(x[1:]) for x in match if x[1][::-1] == x[2]]

if not pairs:
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")
if not mirrored_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirrored_words))
