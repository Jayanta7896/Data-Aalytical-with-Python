#Python program to add two Matrices
def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None

    # Initialize an empty result matrix
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Add corresponding elements from both matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

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

result_matrix = add_matrices(matrix1, matrix2)

if result_matrix is not None:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nSum of Matrices:")
    for row in result_matrix:
        print(row)
