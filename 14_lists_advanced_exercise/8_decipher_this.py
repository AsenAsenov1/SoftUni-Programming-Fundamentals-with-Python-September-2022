message = input().split()

new_message = []

for word in message:
    # find the number
    index = 0
    num_to_list = list(filter(lambda x: x.isdigit(), word))
    number = "".join(num_to_list)

    # find the letters
    word_to_list = list(filter(lambda x: x.isalpha(), word))
    # swap indexes
    word_to_list[0], word_to_list[-1] = word_to_list[-1], word_to_list[0]

    # concat the char of number and the letters
    current_word = "".join(word_to_list)
    final_word = chr(int(number)) + current_word
    new_message.append(final_word)

result = " ".join(new_message)

print(result)
