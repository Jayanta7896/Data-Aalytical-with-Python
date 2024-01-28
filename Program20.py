#Python Program to Split the array and add the first part to the end
def split_and_add(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than the length of the array

    # Split the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]

    # Concatenate the second part with the first part
    result = second_part + first_part
    return result

# Get input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
k = int(input("Enter the number of positions to split and add to the end: "))

# Perform the split and add operation and print the result
result = split_and_add(arr, k)
print(f"The array after splitting and adding is: {result}")
