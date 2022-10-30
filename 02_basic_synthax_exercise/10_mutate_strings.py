first_string = input()
second_string = input()
iterations = len(first_string)
last_word = ""

for letter in range(iterations+1):
    some_text_one = first_string[letter::1]
    some_text_two = second_string[:letter]
    current_word = f"{some_text_two}{some_text_one}"
    if current_word == last_word:
        continue
    if some_text_one == first_string or some_text_two == second_string:
        continue

    else:
        print(current_word)
        last_word = current_word
