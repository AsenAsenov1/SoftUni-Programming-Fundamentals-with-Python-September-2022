words_list = input().split()
words_list = [x.lower() for x in words_list]
word_counter = {word: words_list.count(word) for word in words_list}
odd_list = []

for key, value in word_counter.items():
    if value % 2 == 1:
        odd_list.append(key)

print(*odd_list)

