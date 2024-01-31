#Python Counter| Find all duplicate characters in string
from collections import Counter

def find_duplicate_characters(input_string):
    char_counts = Counter(input_string)
    duplicates = [char for char, count in char_counts.items() if count > 1]
    return duplicates

# Example usage:
input_string = "programming"

result = find_duplicate_characters(input_string)

if result:
    print(f"The duplicate characters in the string '{input_string}' are: {result}")
else:
    print(f"There are no duplicate characters in the string '{input_string}'.")
