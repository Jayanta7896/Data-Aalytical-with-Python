#	Python | Check if a given string is binary string or not
def is_binary_string(input_string):
    for char in input_string:
        if char not in {'0', '1'}:
            return False
    return True

# Example usage:
user_input = input("Enter a string: ")

if is_binary_string(user_input):
    print("The string is a binary string.")
else:
    print("The string is not a binary string.")
