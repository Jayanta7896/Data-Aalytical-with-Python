#Python program for removing i-th character from a string
def remove_ith_character(input_string, i):
    if 0 <= i < len(input_string):
        result = input_string[:i] + input_string[i+1:]
        return result
    else:
        print("Index out of range.")
        return input_string

# Example usage:
original_string = "example"
index_to_remove = 2

result_string = remove_ith_character(original_string, index_to_remove)

print(f"Original String: {original_string}")
print(f"String after removing {index_to_remove}-th character: {result_string}")
