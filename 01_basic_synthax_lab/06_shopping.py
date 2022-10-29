budget = int(input())
input_line = int(input())

while input_line != 'End':
    product_price = int(input_line)
    budget -= product_price
    if budget < 0:
        print("You went in overdraft!")
        break
    input_line = input()
else:
    print("You bought everything needed.")
