animals = input().split(", ")
animals.reverse()
wolf_index = animals.index("wolf")

if wolf_index == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")




