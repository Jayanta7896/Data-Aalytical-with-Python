#Python | Check order of character in string using OrderedDict( )
from collections import OrderedDict

def check_order(input_string, pattern):
    # Create an OrderedDict from the input string
    char_dict = OrderedDict.fromkeys(input_string)

    # Iterate over the pattern and check if characters are in the same order
    for char in pattern:
        if char not in char_dict:
            return False

    return True

# Example usage:
input_str = "Hello, World!"
pattern_to_check = "eoo"

result = check_order(input_str, pattern_to_check)

if result:
    print(f"The characters in the pattern '{pattern_to_check}' appear in order in the string.")
else:
    print(f"The characters in the pattern '{pattern_to_check}' do not appear in order in the string.")
