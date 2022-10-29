n = int(input())

for i in range(n):
    nums = int(input())
    if nums % 2 == 1:
        print(f'{nums} is odd!')
        break
else:
    print("All numbers are even.")


