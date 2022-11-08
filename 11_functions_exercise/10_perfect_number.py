def perfect_num(number1):
    sum1 = 0
    for iteration_num in range(1, number):
        if number % iteration_num == 0:
            sum1 = sum1 + iteration_num
    if sum1 == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_num(number))
