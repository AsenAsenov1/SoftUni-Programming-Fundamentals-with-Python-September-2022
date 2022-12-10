def char_multiplier(text: list):
    number = 0
    short_word, long_word = sorted(text, key=lambda x: len(x))

    if len(short_word) != len(long_word):
        for char in range(len(long_word)):
            if char < len(short_word):
                number += ord(short_word[char]) * ord(long_word[char])
            else:
                number += ord(long_word[char])
        return number
    else:
        for char in range(len(long_word)):
            number += ord(short_word[char]) * ord(long_word[char])
        return number


some_text = input().split(" ")
print(char_multiplier(some_text))
