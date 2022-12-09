def repeat_strings(text: list):
    new_word = ""
    for word in text:
        new_word += word * len(word)
    return new_word


some_text = input().split()
print(repeat_strings(some_text))
