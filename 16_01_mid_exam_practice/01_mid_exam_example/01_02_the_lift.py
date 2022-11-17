people_left = int(input())
state = list(map(int, input().split(" ")))

for number in range(len(state)):
    people_in_current_wagon = state[number]
    diff = 4 - people_in_current_wagon
    if people_in_current_wagon < 4:
        if people_left >= 4:
            state[number] += diff
            people_left -= diff
        else:
            state[number] += people_left
            people_left -= people_left

free_spots = len([x for x in state if x < 4])


if people_left == 0 and free_spots > 0:
    print("The lift has empty spots!")
    print(*state)
elif people_left > 0 and free_spots == 0:
    print(f"There isn't enough space! {people_left} people in a queue!")
    print(*state)
elif free_spots == 0 and people_left == 0:
    print(*state)


