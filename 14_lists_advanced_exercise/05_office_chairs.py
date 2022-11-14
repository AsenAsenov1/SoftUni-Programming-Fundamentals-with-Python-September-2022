number_of_rooms = int(input())
current_room = 0
free = True
total_free = 0

for room in range(number_of_rooms):
    current_parameters = input().split()
    current_room += 1
    chairs_in_room = len(current_parameters[0])
    visitors = int(current_parameters[1])
    diff = abs(chairs_in_room - visitors)
    if visitors > chairs_in_room:
        print(f"{diff} more chairs needed in room {current_room}")
        free = False
    else:
        total_free += diff

    current_parameters.clear()

if free:
    print(f"Game On, {total_free} free chairs left")
