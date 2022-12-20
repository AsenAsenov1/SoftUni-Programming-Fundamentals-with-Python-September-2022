raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    action = command.split(">>>")
    if "Contains" in action:
        substring = action[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif "Flip" in action:
        start_index = int(action[2])
        end_index = int(action[3])
        if "Upper" in action:
            sub = raw_key[start_index:end_index].upper()
            raw_key = raw_key[:start_index] + sub + raw_key[end_index:]
        elif "Lower" in action:
            sub = raw_key[start_index:end_index].lower()
            raw_key = raw_key[:start_index] + sub + raw_key[end_index:]
        print(raw_key)
    elif "Slice" in action:
        start_index = int(action[1])
        end_index = int(action[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
