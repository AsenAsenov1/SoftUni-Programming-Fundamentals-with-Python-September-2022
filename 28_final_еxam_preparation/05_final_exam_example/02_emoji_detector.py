import re

text = input()
cool_threshold = 1
emoji_pattern = r"(\:{2}|\*{2})\b([A-Z]{1}[a-z]{2,})(\b\1)"
threshold_pattern = r"(\d{1})"

threshold_match = re.findall(threshold_pattern, text)
emoji_match = re.findall(emoji_pattern, text)

for number in threshold_match:
    cool_threshold *= int(number)

print(f"Cool threshold: {cool_threshold}")
if emoji_match:
    print(f"{len(emoji_match)} emojis found in the text. The cool ones are:")
    for emoji in emoji_match:
        total_sum = 0
        for char in emoji[1]:
            total_sum += ord(char)
        if total_sum > cool_threshold:
            print("".join(emoji))
