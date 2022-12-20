import re

num_of_barcodes = int(input())
word_pattern = r'\@{1}\#+\b([A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})\b\@{1}\#+'
digit_pattern = r"\d+"

for i in range(num_of_barcodes):
    init_barcode = input()
    word = re.findall(word_pattern, init_barcode)
    digits = re.findall(digit_pattern, "".join(word))
    if word:
        if digits:
            print(f'Product group: {"".join(digits)}')
        else:
            print("Product group: 00")
    else:
        print('Invalid barcode')
