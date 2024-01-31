#import heapq

def find_n_largest_elements(lst, n):
    if n <= 0:
        print("Please provide a positive value for N.")
        return []

    # Use heapq's nlargest function to find the N largest elements
    n_largest_elements = heapq.nlargest(n, lst)

    return n_largest_elements

# Example usage:
my_list = [5, 2, 8, 1, 9, 3]
N = 3

result = find_n_largest_elements(my_list, N)

print(f"The {N} largest elements in the list are: {result}")

import heapq

def find_n_largest_elements(lst, n):
    if n <= 0:
        print("Please provide a positive value for N.")
        return []

    # Use heapq's nlargest function to find the N largest elements
    n_largest_elements = heapq.nlargest(n, lst)

    return n_largest_elements

# Example usage:
my_list = [5, 2, 8, 1, 9, 3]
N = 3

result = find_n_largest_elements(my_list, N)

print(f"The {N} largest elements in the list are: {result}")
