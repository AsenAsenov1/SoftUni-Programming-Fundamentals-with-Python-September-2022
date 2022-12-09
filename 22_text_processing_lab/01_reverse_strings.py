def text_reverse(txt):
    return f"{text} = {txt[::-1]}"


while True:
    text = input()
    if text == 'end':
        break
    print(text_reverse(text))
