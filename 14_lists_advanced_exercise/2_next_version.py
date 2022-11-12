current_version = input().split(".")

current_version_string = "".join(current_version)
next_version_int = int(current_version_string) + 1
next_version_lst = [x for x in str(next_version_int)]
next_version_str = ".".join(next_version_lst)

print(next_version_str)
