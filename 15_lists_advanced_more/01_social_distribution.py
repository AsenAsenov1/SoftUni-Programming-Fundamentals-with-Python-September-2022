population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
wealthiest_persons = sum(x for x in population if x > minimum_wealth)

needed_money = sum([minimum_wealth - x for x in population if x < minimum_wealth])

if wealthiest_persons - needed_money >= minimum_wealth:
    for person in range(len(population)):
        if population[person] <= minimum_wealth:
            population[person] = minimum_wealth
        else:
            population[person] -=

    print(population)
else:
    print("No equal distribution possible")
