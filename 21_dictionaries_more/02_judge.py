contests_info = {}
individual = {}

while True:
    command = input()
    if "no more time" in command:
        break
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests_info:
        contests_info[contest] = {username: points}
        if username not in contests_info.values():
            contests_info[contest][username] = points
    else:
        if username not in contests_info.values():
            contests_info[contest][username] = points
        else:
            if contests_info[contest][username] > points:
                contests_info[contest][username] = points

for content, name_score in contests_info.items():
    counter = 1
    print(f"{content}: {len(name_score)} participants")
    for name, score in sorted(name_score.items(), key=lambda x: (-x[1], x[0])):
        print(f"{counter}. {name} <::> {score}")
        counter += 1
        if name not in individual:
            individual[name] = 0
        individual[name] += score

counter = 1
print("Individual standings:")
for name, score in sorted(individual.items(), key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {name} -> {score}")
    counter += 1

# print(contests_info)
# print(individual)
