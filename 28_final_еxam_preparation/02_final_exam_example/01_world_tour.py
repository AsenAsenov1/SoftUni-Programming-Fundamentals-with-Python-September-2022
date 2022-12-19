stops = input()

while True:
    command = input()
    if command == "Travel":
        break
    action = command.split(":")
    if "Add Stop" in action:
        index, string = action[1:]
        index = int(index)
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]

    elif "Remove Stop" in action:
        start_index = int(action[1])
        stop_index = int(action[2])
        if start_index in range(len(stops)) and stop_index in range(len(stops)):
            remove_word = stops[start_index:stop_index + 1]
            stops = stops.replace(remove_word, "")

    elif "Switch" in action:
        old_string, new_string = action[1:]
        if old_string in stops:
            stops = stops.replace(old_string, new_string, -1)
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
