text = input()

while True:
    command = input()
    if command == "Finish":
        break

    current_command = command.split(" ")
    action = current_command[0]

    if action == "Replace":
        current_character, new_character = current_command[1:]

        for character in text:
            if character == current_character:
                text = text.replace(current_character, new_character)
        print(text)

    elif action == "Cut":
        start_index, end_index = int(current_command[1]), int(current_command[2])

        if start_index in range(len(text)) and end_index in range(len(text)):
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")

    elif action == "Make":
        case = current_command[1]
        if case == "Upper":
            text = text.upper()
        else:
            text = text.lower()
        print(text)

    elif action == "Check":
        substring = current_command[1]
        if substring in text:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif action == "Sum":
        start_sum_index, end_sum_index = int(current_command[1]), int(current_command[2])

        sum = 0
        if start_sum_index in range(len(text)) and end_sum_index in range(len(text)):
            result_string = text[start_sum_index:end_sum_index + 1]
            for symbol in result_string:
                sum += int(ord(symbol))
            if sum > 0:
                print(sum)
        else:
            print("Invalid indices!")
