#Python | Get Kth Column of Matrix
def get_kth_column(matrix, k):
    column = [row[k] for row in matrix]
    return column

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get the 2nd (index 1) column
k = 1
column = get_kth_column(matrix, k)

# Print the column
print(column)
