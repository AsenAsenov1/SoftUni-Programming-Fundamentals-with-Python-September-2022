contests_info_dict = {}
users_info = {}
users_total_score = {}

while True:
    command = input()
    if "end of contests" in command:
        break
    contest, password_contest = command.split(":")
    contests_info_dict[contest] = password_contest

while True:
    command = input()
    if "end of submissions" in command:
        break
    contest, password, username, points = command.split("=>")
    if contest in contests_info_dict.keys():
        if password in contests_info_dict[contest]:
            if username not in users_info.keys():
                users_info[username] = {contest: points}
            if contest not in users_info[username]:
                users_info[username][contest] = points
            else:
                if points > users_info[username][contest]:
                    users_info[username][contest] = points

for usr, total_sum in users_info.items():
    users_total_score[usr] = sum(list(map(int, total_sum.values())))
best_candidate, total_points = list(max(users_total_score.items()))
print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")
users_info = dict(sorted(users_info.items()))
# print(users_info)
for name, courses in users_info.items():
    print(name)
    for course, score in sorted(courses.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {course} -> {score}")
