#Python program to find second largest number in a list
# Define a list
my_list = [5, 2, 8, 1, 9, 3]

# Sort the list in ascending order
sorted_list = sorted(my_list)

# Find the second largest number
if len(sorted_list) >= 2:
    second_largest = sorted_list[-2]
    print(f"The second largest number in the list is: {second_largest}")
else:
    print("The list does not have a second largest number.")
