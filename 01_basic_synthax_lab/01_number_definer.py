input_var = float(input())

if input_var == 0:
    print("zero")
elif input_var > 0:
    if input_var < 1:
        print("small positive")
    elif input_var > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(input_var) < 1:
        print("small negative")
    elif abs(input_var) > 100000:
        print("large negative")
    else:
        print("negative")
