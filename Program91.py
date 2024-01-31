#Python – Replace all occurrences of a substring in a string
def replace_substring(original_string, old_substring, new_substring):
    modified_string = original_string.replace(old_substring, new_substring)
    return modified_string

# Example usage:
input_string = "Hello, world! Hello, Python!"
old_substring = "Hello"
new_substring = "Hi"

result = replace_substring(input_string, old_substring, new_substring)

print("Original String:", input_string)
print("Modified String:", result)
