#Python | Remove empty tuples from a list
# Original list with empty tuples
my_list = [(1, 2), (), (3, 4), (), (), (5, 6)]

# Remove empty tuples using list comprehension
filtered_list = [tup for tup in my_list if tup]

# Print the result
print("Original list:", my_list)
print("List after removing empty tuples:", filtered_list)
