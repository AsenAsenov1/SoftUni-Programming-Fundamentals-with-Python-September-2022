year = int(input())

happy = False
my_set = set()

while not happy:
    year += 1
    for index in str(year):
        my_set.add(index)
    if len(my_set) == len(str(year)):
        happy = True
    else:
        my_set.clear()
print(year)
