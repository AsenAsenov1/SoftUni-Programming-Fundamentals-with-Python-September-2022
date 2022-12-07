submissions = {}
users = {}
banned = False

while True:
    command = input().split("-")
    if "exam finished" in command:
        break
    username = command[0]
    language = command[1]

    if username not in users.keys():
        points = int(command[2])
        users[username] = points
    else:
        if "banned" in command:
            users.pop(username)
            banned = True
        else:
            points = int(command[2])
            if users[username] < points:
                users[username] = points

    if not banned:
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for name, score in users.items():
    print(f"{name} | {score}")
print("Submissions:")
for lng, number in submissions.items():
    print(f"{lng} - {number}")
