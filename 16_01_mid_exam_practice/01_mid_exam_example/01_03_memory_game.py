sequence = input().split()
number_of_turns = 0
win = False

while True:
    command = input()
    if command == "end":
        break

    number_of_turns += 1
    integers = list(map(int, command.split()))
    first_index = int(integers[0])
    second_index = int(integers[1])
    middle_index = len(sequence) // 2
    symbol_1 = sequence[first_index]
    symbol_2 = sequence[second_index]

    if 0 <= first_index < len(sequence) and len(sequence) > second_index >= 0 and first_index != second_index:
        if symbol_1 == symbol_2:
            sequence = [x for x in sequence if x != symbol_1]
            print(f"Congrats! You have found matching elements - {symbol_1}!")
        else:
            print("Try again!")

    else:
        string_to_add = f"-{number_of_turns}a"
        sequence.insert(middle_index, string_to_add)
        sequence.insert(middle_index, string_to_add)
        print("Invalid input! Adding additional elements to the board")

    if len(sequence) == 0:
        print(f"You have won in {number_of_turns} turns!")
        win = True
        break

if not win:
    print(f"Sorry you lose :(")
    print(' '.join(sequence))
