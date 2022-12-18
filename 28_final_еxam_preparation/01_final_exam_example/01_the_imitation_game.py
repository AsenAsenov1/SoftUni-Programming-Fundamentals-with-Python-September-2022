message = input()

while True:
    commands = input().split("|")
    if "Decode" in commands:
        break
    action = commands[0]
    if action == "Move":
        num_of_letters = int(commands[1])
        letters = message[:num_of_letters]
        message = message[num_of_letters:] + letters
    elif action == "Insert":
        index = int(commands[1])
        value = commands[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = commands[1]
        replacement = commands[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
