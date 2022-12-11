def explode(text: str):
    new_string = ""
    strength = 0
    for index in range(len(text)):
        char = text[index]
        if char == ">":
            increase_strength = int(text[index + 1])
            strength += increase_strength
            new_string += ">"
        else:
            if strength > 0:
                strength -= 1
            else:
                new_string += char
    return new_string


text_explode = input()
print(explode(text_explode))
