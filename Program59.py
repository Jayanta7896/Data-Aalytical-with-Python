#Python | Matrix creation of n*n
def create_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    return matrix

# Example: create a 3x3 matrix
n = 3
matrix = create_matrix(n)

# Print the matrix
for row in matrix:
    print(row)
