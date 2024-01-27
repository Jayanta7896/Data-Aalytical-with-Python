#Python program to print all Prime numbers in an Interval?
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    print(f"Prime numbers in the interval [{start}, {end}]:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)

# Example usage:
start_interval = int(input("Enter the start of the interval: "))
end_interval = int(input("Enter the end of the interval: "))

print_primes_in_interval(start_interval, end_interval)
