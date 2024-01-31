#Remove multiple elements from a list in Python
# Original list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Elements to remove
elements_to_remove = [2, 4, 6]

# Create a new list without the specified elements using list comprehension
new_list = [x for x in my_list if x not in elements_to_remove]

# Print the result
print("Original list:", my_list)
print("List after removing elements:", new_list)
