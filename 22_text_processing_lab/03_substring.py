def remove_occurrences(word1, word2):
    while word1 in word2:
        word2 = word2.replace(word1, "")
    return word2


first_word = input()
second_word = input()
print(remove_occurrences(first_word, second_word))
