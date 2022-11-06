def calculate(a: int, b: int):
    if "multiply" in operation:
        return a * b
    elif "divide" in operation:
        return a // b
    elif "add" in operation:
        return a + b
    elif "subtract" in operation:
        return a - b


operation = input()
first_number = int(input())
second_number = int(input())
print(calculate(first_number, second_number))


