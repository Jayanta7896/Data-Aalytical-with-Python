#Python | Sum of number digits in List
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Example usage:
numbers_list = [123, 45, 678, 9]

sum_of_digits_list = [sum_of_digits(num) for num in numbers_list]

print("Original list:", numbers_list)
print("Sum of digits in each number:", sum_of_digits_list)
