def data_type_solve(data_type, value):
    result = 0
    if data_type == "int":
        result = int(value) * 2
    elif data_type == "real":
        result = f"{float(value) * 1.5:.2f}"
    elif data_type == "string":
        result = f"${value}$"
    if result != 0:
        print(result)


input_1 = input()
input_2 = input()
data_type_solve(input_1, input_2)
