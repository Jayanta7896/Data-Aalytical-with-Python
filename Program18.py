#Python Program for array rotation
def left_rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than the length of the array
    rotated_array = arr[k:] + arr[:k]
    return rotated_array

# Get input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
k = int(input("Enter the number of positions to rotate left: "))

# Perform left rotation and print the result
rotated_result = left_rotate_array(arr, k)
print(f"The array after left rotation is: {rotated_result}")
