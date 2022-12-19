import re

pattern = r"([/=])\b([A-Z]{1}[A-Za-z]{2,})\b\1"

places = input()
match = re.findall(pattern, places)
destinations = ["".join(x[1:]) for x in match]
travel_points = sum([len(x) for x in destinations])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
