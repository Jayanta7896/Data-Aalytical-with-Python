#Python program to find simple interest?
def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = P * R * T / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest_result = calculate_simple_interest(principal_amount, interest_rate, time_period)

print(f"The simple interest for principal ${principal_amount}, interest rate {interest_rate}%, and time {time_period} years is: ${simple_interest_result}")
