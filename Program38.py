#Python program to print all even numbers in a range
# Define the range (start, end+1)
start = 1
end = 20

# Print even numbers in the range using a loop
print("Even numbers in the range:")
for num in range(start, end+1):
    if num % 2 == 0:
        print(num)
