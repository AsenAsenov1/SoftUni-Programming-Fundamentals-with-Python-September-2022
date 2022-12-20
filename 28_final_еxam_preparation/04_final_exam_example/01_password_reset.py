init_string = input()

while True:
    command = input()
    if command == "Done":
        break
    action = command.split(" ")
    if "TakeOdd" in action:
        init_string = "".join([str(init_string[x]) for x in range(1, len(init_string), 2)])
        print(init_string)
    elif "Cut" in action:
        index = int(action[1])
        length = int(action[2])
        substring = init_string[index:index + length]
        init_string = init_string.replace(substring, "", 1)
        print(init_string)
    elif "Substitute" in action:
        substring, substitute = action[1:]
        if substring in init_string:
            while substring in init_string:
                init_string = init_string.replace(substring, substitute)
            print(init_string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {init_string}")
