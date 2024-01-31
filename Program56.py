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
    [1, 
