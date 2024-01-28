#Python Program for cube sum of first n natural numbers
def cube_sum(n):
    return sum(i**3 for i in range(1, n + 1))

# Get input from the user
n = int(input("Enter the value of n: "))

# Check for valid input
if n < 1:
    print("Please enter a positive integer.")
else:
    result = cube_sum(n)
    print(f"The cube sum of the first {n} natural numbers is: {result}")
