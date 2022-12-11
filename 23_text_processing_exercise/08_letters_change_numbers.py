def change_nums(text: list):
    text = [x.strip() for x in text]
    numbers_lst = []
    for word in text:
        first_letter = word[0]
        number = int(word[1:-1])
        last_letter = word[-1]
        first_letter_alphabet_position = ord(first_letter.lower()) - 96
        last_letter_alphabet_position = ord(last_letter.lower()) - 96
        if first_letter.isupper():
            number /= first_letter_alphabet_position
        elif first_letter.islower():
            number *= first_letter_alphabet_position
        if last_letter.isupper():
            number -= last_letter_alphabet_position
        elif last_letter.islower():
            number += last_letter_alphabet_position
        numbers_lst.append(number)
    return f"{sum(numbers_lst):.2f}"


symbols = input().split()
print(change_nums(symbols))
