#Adding and Subtracting Matrices in Python
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Example matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Adding matrices
result_addition = add_matrices(matrix_a, matrix_b)
print("Matrix Addition:")
for row in result_addition:
    print(row)

# Subtracting matrices
result_subtraction = subtract_matrices(matrix_a, matrix_b)
print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)
