number1 = input()

special = 0

for i in range(1, int(number1) + 1):
    for digit in str(i):
        special += int(digit)
    if special == 7 or special == 5 or special == 11:
        print(f"{i} -> True")
        special = 0
    else:
        print(f"{i} -> False")
        special = 0
