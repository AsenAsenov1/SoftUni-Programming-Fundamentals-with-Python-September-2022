players_info = {}
players_total_points = {}

while True:
    info = input()
    if info == "Season end":
        break

    if " vs " in info:
        player_1, player_2 = info.split(" vs ")
        if players_info[player_1].values() in players_info[player_2].values():
            pass

    else:
        player, position, points = info.split(" -> ")
        points = int(points)
        if player not in players_info:
            players_info[player] = {position: points}
        else:
            if position not in players_info[player]:
                players_info[player][position] = points
            elif players_info[player][position] < points:
                players_info[player][position] = points
print(players_info)

for player, skill_points in sorted(players_info.items()):
    # print(f"{player}: {sum(skill_points.values())} skill")
    # for skill, points in skill_points.items():
    #     print(f"- {skill} <::> {points}")
