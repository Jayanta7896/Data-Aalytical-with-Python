#Python program to split and join a string
def split_and_join(input_string, delimiter):
    # Split the string into a list of substrings
    split_result = input_string.split(delimiter)

    # Join the substrings into a new string
    join_result = delimiter.join(split_result)

    return split_result, join_result

# Example usage:
original_string = "This is a sample string"
delimiter = " "

split_result, join_result = split_and_join(original_string, delimiter)

print(f"Original String: {original_string}")
print(f"Split Result: {split_result}")
print(f"Join Result: {join_result}")
