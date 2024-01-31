#Python Program to check if given array is Monotonic
def is_monotonic(arr):
    increasing = decreasing = True

    # Check for non-increasing
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            increasing = False
            break

    # Check for non-decreasing
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            decreasing = False
            break

    return increasing or decreasing

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 2, 3, 2]

print(f"Is array1 monotonic? {is_monotonic(array1)}")
print(f"Is array2 monotonic? {is_monotonic(array2)}")
print(f"Is array3 monotonic? {is_monotonic(array3)}")
