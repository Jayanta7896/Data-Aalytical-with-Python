#Python program to interchange first and last elements in a list
def interchange_first_last(lst):
    if len(lst) < 2:
        # No interchange possible for lists with less than two elements
        return lst

    # Interchange the first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]

    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
interchanged_list = interchange_first_last(my_list)

print(f"Original list: {my_list}")
print(f"List after interchange: {interchanged_list}")
