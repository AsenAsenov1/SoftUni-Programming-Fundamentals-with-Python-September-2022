def factorial(num1, num2):
    result1 = 1
    result2 = 1
    for number1 in range(1, num1 + 1):
        result1 *= number1

    for number2 in range(1, num2 + 1):
        result2 *= number2

    return f"{result1 // result2:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial(first_number, second_number))
