lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_broken = lost_fights_count // 2
swords_broken = lost_fights_count // 3
shields_broken = lost_fights_count // 6
armor_broken = shields_broken // 2
if lost_fights_count // 6 == 0:
    shields_broken += 1

expenses = helmet_price * helmets_broken + \
    sword_price * swords_broken + \
    shield_price * shields_broken + \
    armor_price * armor_broken

print(f"Gladiator expenses: {expenses:.2f} aureus")
