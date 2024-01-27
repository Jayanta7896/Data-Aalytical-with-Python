#Python Program for compound interest?
def calculate_compound_interest(principal, rate, time, compounding_frequency):
    # Compound Interest formula: A = P * (1 + r/n)^(nt) - P
    n = compounding_frequency
    compound_interest = principal * (1 + rate / (n * 100))**(n * time) - principal
    return compound_interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))
compounding_frequency = int(input("Enter the compounding frequency per year: "))

compound_interest_result = calculate_compound_interest(principal_amount, interest_rate, time_period, compounding_frequency)

print(f"The compound interest for principal ${principal_amount}, interest rate {interest_rate}%, time {time_period} years, and compounding frequency {compounding_frequency} times per year is: ${compound_interest_result}")
