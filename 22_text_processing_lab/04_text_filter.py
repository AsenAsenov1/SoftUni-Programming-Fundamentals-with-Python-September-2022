def txt_filter(filtered_words_list: list, txt: str):
    for word in filtered_words_list:
        while word in txt:
            replacement = '*' * len(word)
            txt = txt.replace(word, replacement)
    return txt


filtered_words = input().split(", ")
text = input()
print(txt_filter(filtered_words, text))
