names_of_the_gifts = input().split(" ")


while True:
    command = input()
    command_split = command.split()
    if command == "No Money":
        break

    action = command_split[0]
    gift = command_split[1]

    if action == "OutOfStock":
        if gift in names_of_the_gifts:
            names_of_the_gifts = ["None" if x == gift else x for x in names_of_the_gifts]

    if action == "Required":
        index = int(command_split[2])
        if -len(names_of_the_gifts) <= index < len(names_of_the_gifts):
            names_of_the_gifts[index] = gift

    if action == "JustInCase":
        names_of_the_gifts[-1] = gift


names_of_the_gifts = [x for x in names_of_the_gifts if x != "None"]

print(*names_of_the_gifts)
