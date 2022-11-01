snowballs_number = int(input())

max_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for data in range(snowballs_number):
    weight = int(input())
    time = int(input())
    quality = int(input())

    current_value = (weight / time) ** quality
    if current_value > max_value:
        max_weight = weight
        max_time = time
        max_quality = quality
        max_value = current_value

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")




