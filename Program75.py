#	Python | Maximum frequency character in String
def max_frequency_character(input_string):
    # Initialize a dictionary to store character frequencies
    char_freq = {}

    # Count the frequency of each character
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the character with the maximum frequency
    max_freq_char = max(char_freq, key=char_freq.get)

    return max_freq_char

# Example usage:
input_string = "programming"
result = max_frequency_character(input_string)

print("Original String:", input_string)
print("Maximum Frequency Character:", result)
