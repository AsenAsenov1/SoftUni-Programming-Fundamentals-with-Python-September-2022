def replace_chars(text):
    new_word = text[0]
    for char in range(1, len(text)):
        current_char = text[char]
        previous_char = text[char - 1]
        if current_char != previous_char:
            new_word += current_char
    return new_word


unsorted_text = input()
print(replace_chars(unsorted_text))
