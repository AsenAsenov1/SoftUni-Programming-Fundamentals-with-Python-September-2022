
from math import floor


def coord_system(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    result = ""
    line1 = abs(ax1) + abs(ay1) + abs(ax2) + abs(ay2)
    line2 = abs(bx1) + abs(by1) + abs(bx2) + abs(by2)
    if line1 >= line2:
        result = f"({floor(ax2)}, {floor(ay2)})({floor(ax1)}, {floor(ay1)})"
    elif line2 > line1:
        result = f"({floor(bx2)}, {floor(by2)})({floor(bx1)}, {floor(by1)})"

    return result


a_x_1 = float(input())
a_y_1 = float(input())
a_x_2 = float(input())
a_y_2 = float(input())
b_x_1 = float(input())
b_y_1 = float(input())
b_x_2 = float(input())
b_y_2 = float(input())

print(coord_system(a_x_1, a_y_1, a_x_2, a_y_2, b_x_1, b_y_1, b_x_2, b_y_2))
