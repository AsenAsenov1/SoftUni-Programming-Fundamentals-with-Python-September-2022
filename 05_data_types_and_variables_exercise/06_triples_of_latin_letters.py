number_input = int(input())

for number_one in range(number_input):
    for number_two in range(number_input):
        for number_three in range(number_input):
            print(f"{chr(number_one + 97)}{chr(number_two + 97)}{chr(number_three + 97)}")
