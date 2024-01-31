#Python program to print all positive numbers in a range
# Define the range (start, end+1)
start = -10
end = 10

# Print positive numbers in the range using a loop
print("Positive numbers in the range:")
for num in range(start, end+1):
    if num > 0:
        print(num)
