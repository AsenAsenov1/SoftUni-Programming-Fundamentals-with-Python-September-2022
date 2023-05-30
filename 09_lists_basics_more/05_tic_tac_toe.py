def check_player_one(mtrx):
    def check_rows(matrix1):
        for row in matrix1:
            current_row = [x for x in row if x == '1']

            if len(current_row) == 3:
                return True

    def check_cols(matrix1):
        for row in range(len(matrix1)):
            column = []

            for col in range(len(matrix1)):
                if matrix[col][row] == '1':
                    column.append('1')

            if len(column) == 3:
                return True

    def check_diagonal_one(matrix1):
        diagonal = []
        for row in range(len(matrix1)):
            if matrix[row][row] == '1':
                diagonal.append('1')
        if len(diagonal) == 3:
            return True

    def check_diagonal_two(matrix1):
        diagonal = []
        for i in range(2, -1, -1):
            if matrix[2 - i][i] == '1':
                diagonal.append('1')
        if len(diagonal) == 3:
            return True

    rows = check_rows(mtrx)
    cols = check_cols(mtrx)
    diagonal_1 = check_diagonal_one(mtrx)
    diagonal_2 = check_diagonal_two(mtrx)
    if not any([rows, cols, diagonal_1, diagonal_2]):
        return False
    return "First player won"


def check_player_two(mtrx):
    def check_rows(matrix1):
        for row in matrix1:
            current_row = [x for x in row if x == '2']

            if len(current_row) == 3:
                return True
                # print('1')

    def check_cols(matrix1):
        for row in range(len(matrix1)):
            column = []

            for col in range(len(matrix1)):
                if matrix[col][row] == '2':
                    column.append('2')

            if len(column) == 3:
                return True
                # print('2')

    def check_diagonal_one(matrix1):
        diagonal = []
        for row in range(len(matrix1)):
            if matrix[row][row] == '2':
                diagonal.append('2')
        if len(diagonal) == 3:
            return True
            # print('3')

    def check_diagonal_two(matrix1):
        diagonal = []
        for i in range(2, -1, -1):
            if matrix[2 - i][i] == '2':
                diagonal.append('2')
            if len(diagonal) == 3:
                return True
                # print('4')

    rows = check_rows(mtrx)
    cols = check_cols(mtrx)
    diagonal_1 = check_diagonal_one(mtrx)
    diagonal_2 = check_diagonal_two(mtrx)
    if not any([rows, cols, diagonal_1, diagonal_2]):
        return False
    return "Second player won"


############################################
# Define matrix / Main Logic

# Pre-Defined matrix 

# matrix = [
#     ['0', '0', '0'],
#     ['0', '0', '0'],
#     ['0', '0', '0']
# ]

# Input Defined matrix

matrix = []
for _ in range(3):
    row = input().split()
    matrix.append(row)

player_1 = check_player_one(matrix)
player_2 = check_player_two(matrix)

if not player_1 and not player_2:
    print('Draw!')
else:
    if player_1:
        print(player_1)
    elif player_2:
        print(player_2)
