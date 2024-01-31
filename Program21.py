#Python Program for Find reminder of array multiplication divided by n
def find_remainder(arr, n):
    result = 1

    # Calculate the product of all elements in the array
    for element in arr:
        result = (result * element) % n

    return result

# Example usage:
array = [3, 4, 2, 5]
divisor = 7
result = find_remainder(array, divisor)

print(f"The remainder of the array multiplication divided by {divisor} is: {result}")
