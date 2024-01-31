#Remove all duplicates from a given string in Python
def remove_duplicates(input_string):
    seen_chars = set()
    result_string = ""

    for char in input_string:
        if char not in seen_chars:
            seen_chars.add(char)
            result_string += char

    return result_string

# Example usage:
input_string = "programming"
result = remove_duplicates(input_string)

print("Original String:", input_string)
print("String after removing duplicates:", result)
