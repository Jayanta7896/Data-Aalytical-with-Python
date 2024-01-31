#Python | Check for URL in a String
import re

def contains_url(input_string):
    # Regular expression to match common URL patterns
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Search for the URL pattern in the input string
    match = re.search(url_pattern, input_string)

    return bool(match)

# Example usage:
user_input = input("Enter a string: ")

if contains_url(user_input):
    print("The string contains a URL.")
else:
    print("The string does not contain a URL.")
