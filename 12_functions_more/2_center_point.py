def coord_system(x1, y1, x2, y2):
    result = ""
    diff1 = abs(x1) + abs(y1)
    diff2 = abs(x2) + abs(y2)
    if diff1 < diff2:
        result = f"({int(x1)}, {int(y1)})"
    elif diff2 < diff1:
        result = f"({int(x2)}, {int(y2)})"

    else:
        result = f"({round(x1)}, {round(y1)})"

    return result


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(coord_system(x_1, y_1, x_2, y_2))
