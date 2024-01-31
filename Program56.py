#Python program for Matrix Product
import numpy as np

def matrix_product(matrix1, matrix2):
    # Convert input matrices to numpy arrays
    np_matrix1 = np.array(matrix1)
    np_matrix2 = np.array(matrix2)

    # Check if the matrices can be multiplied
    if np_matrix1.shape[1] != np_matrix2.shape[0]:
        print("Matrices cannot be multiplied with the given dimensions.")
        return None

    # Perform matrix multiplication
    result_matrix = np.dot(np_matrix1, np_matrix2)

    return result_matrix.tolist()

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

result_matrix = matrix_product(matrix1, matrix2)

if result_matrix is not None:
    print("Matrix 1:")
    print(np.array(matrix1))

    print("\nMatrix 2:")
    print(np.array(matrix2))

    print("\nProduct of Matrices:")
    print(result_matrix)
