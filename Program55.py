#Python program to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied with the given dimensions.")
        return None

    # Initialize an empty result matrix
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Multiply matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = multiply_matrices(matrix1, matrix2)

if result_matrix is not None:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nProduct of Matrices:")
    for row in result_matrix:
        print(row)
