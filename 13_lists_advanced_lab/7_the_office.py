happiness = list(map(int, input().split()))
factor = int(input())

multiplied_by_factor = [employee * factor for employee in happiness]
average = sum(multiplied_by_factor) // len(happiness)
people_over_average = [x for x in multiplied_by_factor if x > average]

if len(people_over_average) >= len(happiness) / 2:
    print(f"Score: {len(people_over_average)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(people_over_average)}/{len(happiness)}. Employees are not happy!")
