#Python | Check if a Substring is Present in a Given String
def is_substring_present(string, substring):
    return substring in string

# Example usage:
input_string = "Hello, World!"
substring_to_check = "World"

if is_substring_present(input_string, substring_to_check):
    print(f"The substring '{substring_to_check}' is present in the string.")
else:
    print(f"The substring '{substring_to_check}' is not present in the string.")
