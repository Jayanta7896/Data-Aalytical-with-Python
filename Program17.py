#Python Program to find largest element in an array
def find_largest_element(arr):
    if not arr:
        return None  # Return None for an empty array
    else:
        return max(arr)

# Get input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Find and print the largest element in the array
result = find_largest_element(arr)

if result is not None:
    print(f"The largest element in the array is: {result}")
else:
    print("The array is empty.")
