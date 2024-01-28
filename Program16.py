#Python Program to find sum of array
def sum_of_array(arr):
    return sum(arr)

# Get input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Calculate and print the sum of the array
result = sum_of_array(arr)
print(f"The sum of the array is: {result}")
