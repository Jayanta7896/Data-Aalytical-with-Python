#Python program to find factorial of a number.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = int(input("Enter a number to find its factorial: "))

result = factorial(number)
print(f"The factorial of {number} is: {result}")


