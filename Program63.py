#Python program to check whether the string is Symmetrical or Palindrome
def is_symmetrical(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(input_string.split()).lower()

    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(input_string.split()).lower()

    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
user_input = input("Enter a string: ")

if is_symmetrical(user_input):
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
