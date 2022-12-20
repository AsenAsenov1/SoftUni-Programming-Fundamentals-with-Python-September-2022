concealed_message = input()

while True:
    command = input()
    if "Reveal" in command:
        break
    action = command.split(":|:")
    if "InsertSpace" in action:
        index = int(action[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif "Reverse" in action:
        substring = action[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif "ChangeAll" in action:
        substring, replacement = action[1:]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")
