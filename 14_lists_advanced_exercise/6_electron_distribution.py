number_of_electrons = int(input())

lst_of_electrons = []
shell = 0

while sum(lst_of_electrons) < number_of_electrons:
    shell += 1
    current_shell_electrons = 2 * shell ** 2  # 2n^2
    if current_shell_electrons + sum(lst_of_electrons) < number_of_electrons:
        lst_of_electrons.append(current_shell_electrons)
    else:
        lst_of_electrons.append(number_of_electrons - sum(lst_of_electrons))

print(lst_of_electrons)
