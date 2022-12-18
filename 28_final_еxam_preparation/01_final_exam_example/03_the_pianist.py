number = int(input())
pieces = {}

for num in range(1, number + 1):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input()
    if "Stop" in command:
        break
    action = command.split("|")
    if "Add" in action:
        piece, composer, key = action[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif "Remove" in action:
        piece = action[1]
        if piece in pieces:
            print(f"Successfully removed {piece}!")
            pieces.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif "ChangeKey" in action:
        piece, new_key = action[1:]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, composer_key in pieces.items():
    print(f"{piece} -> Composer: {composer_key['composer']}, Key: {composer_key['key']}")
