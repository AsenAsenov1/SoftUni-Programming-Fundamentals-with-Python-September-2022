number_of_lines = int(input())

capacity = 255
litres_counted = 0

for litres in range(number_of_lines):
    litres_input = int(input())
    if litres_input + litres_counted > 255:
        print("Insufficient capacity!")
    else:
        litres_counted += litres_input

print(litres_counted)

