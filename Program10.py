#Python Program for n-th Fibonacci number?
def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Get input from the user
n = int(input("Enter the value of n: "))

# Check for valid input
if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is: {result}")
