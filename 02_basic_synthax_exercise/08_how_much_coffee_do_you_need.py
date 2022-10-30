command = input()
coffees_needed = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffees_needed += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffees_needed += 2
    else:
        command = input()
        continue
    command = input()

if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)
