def char_convert(symbol1, symbol2):
    char_list = []
    for symbol in range(ord(symbol1) + 1, ord(symbol2)):
        char_list.append(chr(symbol))
    return " ".join(char_list)


start_char = input()
stop_char = input()

print(char_convert(start_char, stop_char))
