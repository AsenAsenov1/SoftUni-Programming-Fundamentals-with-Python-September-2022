keys = list(map(int, input().split()))

while True:
    current_string = input()
    if "find" in current_string:
        break
    new_string = ''
    for key in keys:
        for char in current_string:
            # new_string += chr(ord(char) - key)
            print(chr(ord(char)-6))
        print(new_string)
