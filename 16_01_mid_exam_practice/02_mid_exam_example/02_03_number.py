integers = list(map(int, input().split()))

average = round(sum(integers) / len(integers))
above_average = sorted([x for x in integers if x > average], reverse=True)
top_5 = above_average[:5]

if len(above_average) == 0:
    print("No")
else:
    print(*top_5)
