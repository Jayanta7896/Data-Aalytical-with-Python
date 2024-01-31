#Ways to remove i’th character from string in Python
def remove_ith_char(string, i):
    # Slice the string to exclude the ith character
    result = string[:i] + string[i+1:]
    return result

# Example usage:
input_string = "example"
i_to_remove = 2
result = remove_ith_char(input_string, i_to_remove)
print("Original String:", input_string)
print("String after removing {}-th character:".format(i_to_remove), result)
