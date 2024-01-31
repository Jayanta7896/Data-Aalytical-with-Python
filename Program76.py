#Python | Program to check if a string contains any special character
def contains_special_characters(input_string):
    # Define a set of special characters
    special_chars = set("!@#$%^&*()-_+=[]{}|;:'\",.<>?/`~")

    # Check if any character in the input string is a special character
    for char in input_string:
        if char in special_chars:
            return True

    # If no special character is found
    return False

# Example usage:
user_input = input("Enter a string: ")

if contains_special_characters(user_input):
    print("The string contains special characters.")
else:
    print("The string does not contain any special characters.")
