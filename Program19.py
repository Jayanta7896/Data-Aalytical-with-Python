#Python Program for Reversal algorithm for array rotation
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than the length of the array

    # Reverse the elements of the first part
    reverse_array(arr, 0, k - 1)

    # Reverse the elements of the second part
    reverse_array(arr, k, n - 1)

    # Reverse the entire array
    reverse_array(arr, 0, n - 1)

# Get input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
k = int(input("Enter the number of positions to rotate left: "))

# Perform array rotation using reversal algorithm and print the result
rotate_array(arr, k)
print(f"The array after rotation is: {arr}")
