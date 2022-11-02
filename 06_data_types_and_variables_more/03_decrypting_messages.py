key = int(input())
num = int(input())

word = ""

for i in range(num):
    symbol = input()
    word += chr(ord(symbol) + key)
print(word)

