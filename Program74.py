#Python – Least Frequent Character in String
def least_frequent_character(input_string):
    # Initialize a dictionary to store character frequencies
    char_freq = {}

    # Count the frequency of each character
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the least frequent character
    least_frequent_char = min(char_freq, key=char_freq.get)

    return least_frequent_char

# Example usage:
input_string = "programming"
result = least_frequent_character(input_string)

print("Original String:", input_string)
print("Least Frequent Character:", result)
