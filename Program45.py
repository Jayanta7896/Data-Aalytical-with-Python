#Python – Remove empty List from List
# Original list with empty lists
my_list = [1, [], 3, [], 5, [], 7]

# Remove empty lists using list comprehension
filtered_list = [x for x in my_list if x]

# Print the result
print("Original list:", my_list)
print("List after removing empty lists:", filtered_list)
