def find_emoji(text):
    emojis_lst = []
    emoji = ""
    for char in range(len(text)):
        current_char = text[char]
        if current_char == ":":
            next_char = text[char + 1]
            if not next_char.isdigit():
                emoji = current_char + next_char
                emojis_lst.append(emoji)
                emoji = ""
    return "\n".join(emojis_lst)


sentence = input()
print(find_emoji(sentence))
