#Python program to print odd numbers in a List
# Define a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print odd numbers using a loop
print("Odd numbers in the list:")
for num in my_list:
    if num % 2 != 0:
        print(num)
