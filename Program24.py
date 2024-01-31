#Python program to swap two elements in a list
def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        # Check if indices are valid
        lst[index1], lst[index2] = lst[index2], lst[index1]
    else:
        print("Invalid indices. Please provide valid indices within the list bounds.")

# Example usage:
my_list = [1, 2, 3, 4, 5]
index_to_swap1 = 1
index_to_swap2 = 3

print(f"Original list: {my_list}")
swap_elements(my_list, index_to_swap1, index_to_swap2)
print(f"List after swapping elements at indices {index_to_swap1} and {index_to_swap2}: {my_list}")
