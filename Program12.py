#Python Program for n\’th multiple of a number in Fibonacci Series?
def fibonacci_multiple(n, multiple_of):
    fib = [0, 1]
    
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        
        if next_fib % multiple_of == 0:
            n -= 1

    return fib[-1]

# Get input from the user
n = int(input("Enter the value of n: "))
multiple_of = int(input("Enter the number to find its multiple in Fibonacci series: "))

# Check for valid input
if n <= 0 or multiple_of <= 0:
    print("Please enter positive integers for n and the number.")
else:
    result = fibonacci_multiple(n, multiple_of)
    print(f"The {n}-th multiple of {multiple_of} in the Fibonacci series is: {result}")
