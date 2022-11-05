numbers = input().split()
message_string = input()
message_string = [x for x in message_string]

indexes = []
decoded_message = ""

for num in numbers:
    index = 0
    for chars in num:
        index += int(chars)
    indexes.append(index)

for inx in indexes:
    if inx >= len(message_string):
        valid_inx = inx - len(message_string)
        char = str(message_string[valid_inx])
        decoded_message += char
        message_string.pop(valid_inx)
    else:
        decoded_message += message_string[inx]
        message_string.pop(inx)

print(decoded_message)
