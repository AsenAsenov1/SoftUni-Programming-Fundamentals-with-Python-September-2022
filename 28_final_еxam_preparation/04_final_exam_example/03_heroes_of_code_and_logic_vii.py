number_of_heroes = int(input())
heroes_info = {}
max_hp = 100
max_mana = 200

for i in range(number_of_heroes):
    hero_name, hp, mana = input().split()
    heroes_info[hero_name] = {"hp": int(hp), "mana": int(mana)}

while True:
    command = input()
    if "End" in command:
        break
    action = command.split(" - ")

    if "CastSpell" in action:
        hero_name, mana_needed, spell_name = action[1:]
        if heroes_info[hero_name]["mana"] >= int(mana_needed):
            heroes_info[hero_name]["mana"] -= int(mana_needed)
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif "TakeDamage" in action:
        hero_name, damage, attacker = action[1:]
        heroes_info[hero_name]["hp"] -= int(damage)
        if heroes_info[hero_name]["hp"] > 0:
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_info[hero_name]['hp']} HP left!")
        else:
            heroes_info.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif "Recharge" in action:
        hero_name, amount = action[1:]
        if heroes_info[hero_name]["mana"] + int(amount) > max_mana:
            increased_mana = max_mana - heroes_info[hero_name]["mana"]
            heroes_info[hero_name]["mana"] = max_mana
            print(f"{hero_name} recharged for {increased_mana} MP!")
        else:
            heroes_info[hero_name]["mana"] += int(amount)
            print(f"{hero_name} recharged for {amount} MP!")

    elif "Heal" in action:
        hero_name, amount = action[1:]
        if heroes_info[hero_name]["hp"] + int(amount) > max_hp:
            increased_hp = max_hp - heroes_info[hero_name]["hp"]
            heroes_info[hero_name]["hp"] = max_hp
            print(f"{hero_name} healed for {increased_hp} HP!")
        else:
            heroes_info[hero_name]["hp"] += int(amount)
            print(f"{hero_name} healed for {amount} HP!")

for hero, hp_mana in heroes_info.items():
    print(f"{hero}\n  HP: {hp_mana['hp']}\n  MP: {hp_mana['mana']}")
