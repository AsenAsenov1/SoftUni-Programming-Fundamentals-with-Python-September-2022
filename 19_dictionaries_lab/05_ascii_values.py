input_words = input().split(", ")

dictionary_of_chars = {key: ord(key) for key in input_words}
print(dictionary_of_chars)


