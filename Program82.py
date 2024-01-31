#Python program to find uncommon words from two Strings
def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())

    uncommon_words = words1.symmetric_difference(words2)

    return uncommon_words

# Example usage:
string1 = "This is the first string"
string2 = "This is the second string with some different words"

result = find_uncommon_words(string1, string2)

print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Uncommon words: {result}")
