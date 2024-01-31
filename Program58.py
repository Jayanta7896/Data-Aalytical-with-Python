#Transpose a matrix in Single line in Python
import numpy as np

# Example matrix as a NumPy array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transpose the matrix in a single line
transposed_matrix = np.transpose(matrix)
# Alternatively, you can use the T attribute
# transposed_matrix = matrix.T

print("Original Matrix:")
print(matrix)

print("\nTransposed Matrix:")
print(transposed_matrix)
