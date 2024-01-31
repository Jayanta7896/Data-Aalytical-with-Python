#Python | Sort the values of first list using second list
# Two lists
first_list = [3, 1, 4, 2]
second_list = ['c', 'a', 'd', 'b']

# Sort the first list based on the values of the second list
sorted_lists = sorted(zip(second_list, first_list))

# Unpack the sorted pairs
sorted_second_list, sorted_first_list = zip(*sorted_lists)

# Print the result
print("Original Lists:")
print("First List:", first_list)
print("Second List:", second_list)

print("\nSorted Lists based on the Second List:")
print("Sorted First List:", list(sorted_first_list))
print("Sorted Second List:", list(sorted_second_list))
