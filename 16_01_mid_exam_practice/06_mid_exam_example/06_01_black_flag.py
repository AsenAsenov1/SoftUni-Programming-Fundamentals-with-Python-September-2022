days_of_the_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())  # target

collected = 0

for day in range(1, days_of_the_plunder + 1):
    collected += daily_plunder
    if day % 3 == 0:
        collected += daily_plunder * 0.50  # 50%
    if day % 5 == 0:
        collected *= 0.70  # lose 30%

percentage = (collected / expected_plunder) * 100
if collected >= expected_plunder:
    print(f"Ahoy! {collected:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")
