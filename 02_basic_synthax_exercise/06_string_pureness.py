iterations = int(input())

for string in range(iterations):
    str_input = input()
    if "_" in str_input or "." in str_input or "," in str_input:
        print(f"{str_input} is not pure!")

    else:
        print(f"{str_input} is pure.")
