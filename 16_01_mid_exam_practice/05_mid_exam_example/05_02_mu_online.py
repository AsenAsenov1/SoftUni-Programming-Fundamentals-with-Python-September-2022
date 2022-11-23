rooms = input().split("|")

health = 100
bitcoins = 0
alive = True
room_num = 0
for room in rooms:
    room_num += 1
    command = ""
    damage_str = ""

    for chars in room:
        if chars.isalpha():
            command += chars
        elif chars.isalnum():
            damage_str += chars
    damage = int(damage_str)
    potion = int(damage_str)
    bitcoin_found = (int(damage_str))
    monster = command

    if command == "potion":
        if potion + health > 100:
            healed_amount = 100 - health
            health = 100

        else:
            healed_amount = potion
            health += potion
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        print(f"You found {bitcoin_found} bitcoins.")
        bitcoins += bitcoin_found

    else:
        if health - damage <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_num}")
            alive = False
            break

        else:
            health -= damage
            print(f"You slayed {monster}.")


if alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
