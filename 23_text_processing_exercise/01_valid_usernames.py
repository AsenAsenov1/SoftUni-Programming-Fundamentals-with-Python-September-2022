def valid_usernames(usernames: list):
    valid_names = []
    chars_valid = False
    for name in usernames:
        if 3 <= len(name) <= 16:
            for char in name:
                if char.isalnum() or "_" in char or "-" in char:
                    chars_valid = True
                else:
                    chars_valid = False
                    break
            if chars_valid:
                valid_names.append(name)
    return "\n".join(valid_names)


names_list = input().split(", ")
print(valid_usernames(names_list))
