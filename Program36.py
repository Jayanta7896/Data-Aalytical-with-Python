#Python program to print even numbers in a list
# Define a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print even numbers using a loop
print("Even numbers in the list:")
for num in my_list:
    if num % 2 == 0:
        print(num)
