#Python | Count the Number of matching characters in a pair of string
def count_matching_characters(str1, str2):
    # Convert strings to sets of characters
    set1 = set(str1)
    set2 = set(str2)

    # Find the common characters
    common_characters = set1.intersection(set2)

    # Count the number of common characters
    count = len(common_characters)

    return count, common_characters

# Example usage:
string1 = "hello"
string2 = "world"
result_count, result_characters = count_matching_characters(string1, string2)

print(f"Number of matching characters: {result_count}")
print(f"Matching characters: {result_characters}")
