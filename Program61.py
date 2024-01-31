#Python – Vertical Concatenation in Matrix
def vertical_concatenate(matrix1, matrix2):
    result = matrix1 + matrix2
    return result

# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8, 9],
    [10, 11, 12]
]

# Concatenate vertically
result_concatenation = vertical_concatenate(matrix_a, matrix_b)

# Print the result
for row in result_concatenation:
    print(row)
