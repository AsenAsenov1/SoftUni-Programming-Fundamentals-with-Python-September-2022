text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

filtered_text = [x for x in text if x.lower() not in vowels]

print("".join(filtered_text))
