#Python Program for How to check if a given number is Fibonacci number?
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def is_fibonacci(number):
    if number < 0:
        return False
    
    # Check if 5n^2 + 4 or 5n^2 - 4 is a perfect square
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is a Fibonacci number
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
