#Python – Replace duplicate Occurrence in String
def replace_duplicate_occurrence(input_string):
    result = ""
    seen_chars = set()

    for char in input_string:
        if char not in seen_chars:
            seen_chars.add(char)
            result += char
        else:
            result += '$'  # Replace duplicate occurrence with '$' or any other character

    return result

# Example usage:
input_string = "programming"
result = replace_duplicate_occurrence(input_string)

print("Original String:", input_string)
print("String after replacing duplicate occurrences:", result)
