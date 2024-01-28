#Python Program for Sum of squares of first n natural numbers
def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Get input from the user
n = int(input("Enter the value of n: "))

# Check for valid input
if n < 1:
    print("Please enter a positive integer.")
else:
    result = sum_of_squares(n)
    print(f"The sum of the squares of the first {n} natural numbers is: {result}")
