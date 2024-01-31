#Python program to print positive numbers in a list
# Define a list with both positive and negative numbers
my_list = [1, -2, 3, -4, 5, -6, 7, -8, 9]

# Print positive numbers using a loop
print("Positive numbers in the list:")
for num in my_list:
    if num > 0:
        print(num)
