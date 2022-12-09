def symbol_filter(single_str: str):
    digits = ""
    letters = ""
    symbols = ""
    for char in single_str:
        if char.isdigit():
            digits += char
        elif char.isalpha():
            letters += char
        else:
            symbols += char
    return "\n".join([digits, letters, symbols])


example_str = input()
print(symbol_filter(example_str))
